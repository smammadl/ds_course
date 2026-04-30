import time
import torch
import torchmetrics
import torch.nn as nn
import numpy as np
import matplotlib.pyplot as plt

def train_one_epoch(
	model, 
	optimizer, 
	criterion, 
	metric, 
	train_loader, 
	clip_grad_norm,
	device
	):
	losses = []
	metric.reset()
	model.train()
	for X_batch, y_batch in train_loader:
		X_batch, y_batch = X_batch.to(device), y_batch.to(device)
		y_pred = model(X_batch)
		loss = criterion(y_pred, y_batch)
		losses.append(loss.item())
		loss.backward()
		if clip_grad_norm is not None:
			nn.utils.clip_grad_norm_(model.parameters(), max_norm=clip_grad_norm)
		optimizer.step()
		optimizer.zero_grad()
		metric.update(y_pred, y_batch)
	
	train_loss = np.mean(losses)
	train_metric = metric.compute().item()
	return train_loss, train_metric

def evaluate_one_epoch(
	model, 
	metric, 
	valid_loader, 
	device
	):
	model.eval()
	metric.reset()
	with torch.no_grad():
		for X_batch, y_batch in valid_loader:
			X_batch, y_batch = X_batch.to(device), y_batch.to(device)
			y_pred = model(X_batch)
			metric.update(y_pred, y_batch)
	valid_metric = metric.compute().item()
	return valid_metric

def scheduler_lr(epoch, optimizer, scheduler, warmup_scheduler, valid_metric):
	if scheduler is not None:
		if epoch >= (warmup_scheduler.total_iters if warmup_scheduler is not None else 0):
			if isinstance(scheduler, torch.optim.lr_scheduler.ReduceLROnPlateau):
				scheduler.step(valid_metric)
			else:
				scheduler.step()
	learning_rate = optimizer.param_groups[0]["lr"]
	return learning_rate

def train(
	model, 
	optimizer, 
	criterion, 
	metric, 
	train_loader, 
	valid_loader, 
	n_epochs, 
	warmup_scheduler=None, 
	scheduler=None, 
	patience=None,
	checkpoint_path='best_model.pt',
	clip_grad_norm=None,
    device='cpu'
	):
	history = {
		'train_losses' : [],
		'train_metrics' : [],
		'valid_metrics' : [],
		'learning_rates' : [],
	}
	best_epoch = 0
	best_valid_metric = float('-inf') if metric.higher_is_better else float('inf')
	patience_counter = 0
	
	for epoch in range(n_epochs):
		if warmup_scheduler is not None:
			warmup_scheduler.step()

		#--------------------------------------------
		#                  Training
		#--------------------------------------------
		t0 = time.time()
		train_loss, train_metric = train_one_epoch(
			model, optimizer, criterion, metric, train_loader, clip_grad_norm, device
		)	

		#--------------------------------------------
		#                 Evaluation
		#--------------------------------------------
		valid_metric = evaluate_one_epoch(
			model, metric, valid_loader, device
		)

		#---------------------------------------------
		#                 Checkpoint
		#---------------------------------------------
		is_best = (valid_metric > best_valid_metric) if metric.higher_is_better else (valid_metric < best_valid_metric)

		if is_best:
			torch.save(model.state_dict(), checkpoint_path)
			best_valid_metric = valid_metric
			best_epoch = epoch + 1

		#---------------------------------------------
		#                 Scheduling
		#---------------------------------------------
		learning_rate = scheduler_lr(epoch, optimizer, scheduler, warmup_scheduler, valid_metric)

		#---------------------------------------------
		#                 Logging
		#---------------------------------------------
		history['train_losses'].append(train_loss)
		history['train_metrics'].append(train_metric)
		history['valid_metrics'].append(valid_metric)
		history['learning_rates'].append(learning_rate)
		print(
			(f'Epoch: {epoch+1}/{n_epochs}, ')
			+(f'Train Loss: {round(train_loss,3)}, ')
			+(f'Train Metric: {round(train_metric,3)}, ') 
			+(f'Valid Metric: {round(valid_metric,3)}, ')
			+(f'Learning Rate: {learning_rate:.3f}, ' if (scheduler or warmup_scheduler) else '')
			# # +f'Best Valid Metric: {best_valid_metric:.3f}, '
			+(f'Time: {round(time.time()-t0,2)}s')
		)
		if is_best:
			print(f"\tCheckpoint, valid metric: {best_valid_metric:.3f}")

		#---------------------------------------------
		#                 Early Stopping
		#---------------------------------------------
		if patience is not None:
			if is_best:
				patience_counter = 0
			else:
				patience_counter += 1
				if patience_counter >= patience:
					print(f"Early stopping, best valid metric: {best_valid_metric:.3f}, epoch: {best_epoch}")
					break

	print(f"Restoring best model from epoch {best_epoch} with valid metric: {best_valid_metric:.3f}")
	model.load_state_dict(torch.load(checkpoint_path))

	return history

def plot_history(history, metric):
	n_epochs = len(history['train_metrics'])

	fig, ax = plt.subplots(1, 2, figsize=(12, 4))
	ax[0].plot(np.arange(n_epochs) + 1, history['train_metrics'], linestyle='--', color='r', marker='.', label='Train')
	ax[0].plot(np.arange(n_epochs) + 1, history['valid_metrics'], linestyle='--', color='b', marker='.', label='Valid')
	ax[0].legend()
	ax[0].grid()
	ax[0].set_xlabel('Epochs')
	ax[0].set_ylabel(f'{metric.__class__.__name__}')
	ax[0].set_title('Training and Validation Metrics')
	ax[1].plot(np.arange(n_epochs) + 1, history['learning_rates'], linestyle='--', color='r', marker='.', label='Learning Rate')
	ax[1].legend()
	ax[1].grid()
	ax[1].set_xlabel('Epochs')
	ax[1].set_ylabel('Learning Rate')
	ax[1].set_title('Learning Rate')
	plt.tight_layout()
	plt.show()