import torch
import torch.nn as nn


class GCR(nn.Module):
    def __init__(self, g, C, latent_dim):
        super().__init__()
        self.g = g
        self.C = C
        self.latent_dim = latent_dim

    def classify(self, z):
        logits = self.C(self.g.vae(z)).squeeze()
        return logits

    def classify_x(self, x):
        logits = self.C(x).squeeze()
        return logits

    def generate_images(self, g_z_sampled, is_detached=True):
        """Generate images from g_z_sampled or dataset"""
        # Synthesize the result from z
        img = g_z_sampled
        return img.detach() if is_detached else img

    def get_cond_energy(self, z, y):
        logits = self.classify(z)
        energy_output = torch.gather(logits, 1, y[:, None]).squeeze() - logits.logsumexp(1)
        return energy_output

    def forward(self, z, y):
        energy_output = self.get_cond_energy(z, y) - torch.linalg.norm(z, dim=1) ** 2 * 0.5
        return energy_output


