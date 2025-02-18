import { defineConfig } from '@playwright/test';

export default defineConfig({
  // Directory for test files
  testDir: './scripts',

  // General settings
  timeout: 30000, // 30 seconds timeout for each test
  retries: 2, // Retry failed tests up to 2 times

  // Reporting and tracing
  reporter: 'html', // Generate an HTML report after test execution
  trace: 'on-first-retry', // Capture a trace only on the first retry

  // Global settings for all browsers
  use: {
    headless: false, // Run tests with a visible browser window
    viewport: { width: 1280, height: 720 },
    ignoreHTTPSErrors: true,
    screenshot: 'only-on-failure', // Take screenshots only if a test fails
    video: 'retain-on-failure', // Record video only when a test fails
  },

  // Browser-specific configurations
  projects: [
    {
      name: 'chromium',
      use: { browserName: 'chromium' },
    },
    {
      name: 'firefox',
      use: { browserName: 'firefox' },
    },
    {
      name: 'webkit',
      use: { browserName: 'webkit' },
    },
  ],

  // Parallel execution settings
  workers: 4, // Run tests with 4 parallel workers

  // Output paths for reports and artifacts
  outputDir: 'scripts-results/',
});