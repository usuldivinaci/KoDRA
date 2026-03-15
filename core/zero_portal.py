# -*- coding: utf-8 -*-
"""
Zero-Portal: At the service of KODra.
The Portal executes the Law — it does not replace it.
∀x ∈ M,  x → 𝟎 → U(x)   — KODra is the sole master.
"""
import torch
import time
import sys

from core.unicity_lib import UnicityKernel, _project_to_kernel_dim, KERNEL_DIM


class ZeroPortal:
    """
    Engine of Transition — at the service of KODra.
    Uses UnicityKernel (KODra law) as the sole transformation.
    Finds the fixed point: state such that state ≈ U(state).
    """
    def __init__(self, unicity_kernel=None, dimension=64):
        self.dimension = dimension
        self.unicity_kernel = unicity_kernel or UnicityKernel(dim=dimension)
        self._original_dim = None

    def _prepare_input(self, x_input, verbose=True):
        """Project input to KODra kernel dimension (service of the Law)."""
        raw_dim = x_input.shape[0] if len(x_input.shape) == 1 else x_input.view(-1).shape[0]
        target_dim = self.unicity_kernel.dim
        x_flat = x_input.view(-1).float()
        if raw_dim != target_dim and verbose and raw_dim > target_dim:
            print(f"[*] [0-PORTAL] KODra projection: {raw_dim:,}D → {target_dim}D (Law governs)")
        x_proj = _project_to_kernel_dim(x_flat, target_dim)
        self._original_dim = raw_dim
        return x_proj, target_dim

    def unicity_convergence(self, x_input, unicity_kernel=None, steps=20, tolerance=1e-6,
                            lbfgs_max_iter=20, verbose=True, plateau_patience=50):
        """
        Converges x toward U(x) — fixed point of the KODra law.
        KODra décide d'arrêter si: tol atteinte OU plateau détecté (convergence naturelle).
        """
        kernel = unicity_kernel or self.unicity_kernel
        self.unicity_kernel = kernel
        x_flat, current_dim = self._prepare_input(x_input, verbose)

        state = torch.nn.Parameter(x_flat.clone().detach().float())
        optimizer = torch.optim.LBFGS([state], lr=0.1, max_iter=lbfgs_max_iter)
        history = []
        best_loss = float('inf')

        if verbose:
            print(f"[*] [0-PORTAL] KODra MASTER. Dimension: {current_dim}")
            print(f"[*] TARGET: Fixed point U(x) (Unicity) | steps={steps} tol={tolerance}")

        def closure():
            optimizer.zero_grad()
            projected = kernel(state)
            unicity_gap = torch.norm(state - projected)
            norm_loss = (torch.norm(state) - 1.0) ** 2
            total_energy = unicity_gap + norm_loss
            total_energy.backward()
            return total_energy

        for i in range(steps):
            loss = optimizer.step(closure)
            loss_val = loss.item()
            history.append(loss_val)
            best_loss = min(best_loss, loss_val)

            if verbose:
                coherence = 1.0 / (1.0 + loss_val)
                bar_len = min(20, int(coherence * 20))
                bar = "█" * bar_len + "░" * (20 - bar_len)
                sys.stdout.write(f"\r[TRANSITION {i:02d}] {bar} Coherence: {coherence:.4f} loss={loss_val:.2e}")
                sys.stdout.flush()
                time.sleep(0.03)

            if loss_val < tolerance:
                if verbose:
                    print(f"\n[*] CONVERGED (tol={tolerance}) at step {i+1}")
                break
            if i >= plateau_patience and len(history) >= plateau_patience:
                recent = history[-plateau_patience:]
                if max(recent) - min(recent) < 1e-8 * (1 + abs(min(recent))):
                    if verbose:
                        print(f"\n[*] PLATEAU (KODra) at step {i+1} — Portal stable")
                    break

        if verbose and loss_val >= tolerance and i >= steps - 1:
            print("\n[*] TRANSITION COMPLETE.")

        return state.detach(), history

    def unicity_convergence_track(self, x_input, unicity_kernel=None, steps=20, tolerance=1e-6,
                                   lbfgs_max_iter=20, verbose=True, plateau_patience=50):
        """
        Same as unicity_convergence but also returns correlation_history and ram_history.
        KODra décide d'arrêter si: tol atteinte OU plateau détecté.
        """
        try:
            import psutil
        except ImportError:
            psutil = None
        import os

        kernel = unicity_kernel or self.unicity_kernel
        self.unicity_kernel = kernel
        x_flat, current_dim = self._prepare_input(x_input, verbose)

        state = torch.nn.Parameter(x_flat.clone().detach().float())
        optimizer = torch.optim.LBFGS([state], lr=0.1, max_iter=lbfgs_max_iter)
        history = []
        correlation_history = []
        ram_history = []

        def closure():
            optimizer.zero_grad()
            projected = kernel(state)
            unicity_gap = torch.norm(state - projected)
            norm_loss = (torch.norm(state) - 1.0) ** 2
            total_energy = unicity_gap + norm_loss
            total_energy.backward()
            return total_energy

        if verbose:
            print(f"[*] [0-PORTAL] KODra MASTER. Dimension: {current_dim}")
            print(f"[*] TARGET: U(x) (Unicity) | steps={steps} tol={tolerance}")

        h_max = 1e-9
        for i in range(steps):
            loss = optimizer.step(closure)
            loss_val = loss.item()
            history.append(loss_val)
            h_max = max(h_max, loss_val)
            correlation_history.append(-1.0 * (loss_val / h_max) if h_max > 0 else 0.0)
            if psutil:
                ram_history.append(psutil.Process(os.getpid()).memory_info().rss / (1024 * 1024))
            else:
                ram_history.append(0.0)

            if verbose:
                coherence = 1.0 / (1.0 + loss_val)
                bar_len = min(20, int(coherence * 20))
                bar = "█" * bar_len + "░" * (20 - bar_len)
                sys.stdout.write(f"\r[TRANSITION {i:02d}] {bar} Coherence: {coherence:.4f} loss={loss_val:.2e}")
                sys.stdout.flush()
                time.sleep(0.03)

            if loss_val < tolerance:
                if verbose:
                    print(f"\n[*] CONVERGED (tol={tolerance}) at step {i+1}")
                break
            if i >= plateau_patience and len(history) >= plateau_patience:
                recent = history[-plateau_patience:]
                if max(recent) - min(recent) < 1e-8 * (1 + abs(min(recent))):
                    if verbose:
                        print(f"\n[*] PLATEAU (KODra) at step {i+1} — Portal stable")
                    break

        if verbose and loss_val >= tolerance and i >= steps - 1:
            print("\n[*] TRANSITION COMPLETE.")

        return state.detach(), history, correlation_history, ram_history
