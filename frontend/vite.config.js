import { sveltekit } from '@sveltejs/kit/vite';
import { defineConfig } from 'vite';

export default defineConfig({
  plugins: [sveltekit()],
  server: {
    host: '0.0.0.0',       // expose dev server to Docker / WSL2
    port: 5173,
    strictPort: true,       // fail if port is taken
    watch: {
      usePolling: true,     // WSL2/Docker-friendly
      interval: 100         // poll every 100ms
    }
  }
});
