---
title: Interactive Demo
description: "Try social-links Python library in your browser. No installation required. Test URL validation, platform detection, and URL sanitization for LinkedIn, Instagram, GitHub, Twitter, Facebook, and 65+ social platforms."
keywords:
  - interactive demo
  - test URL validator
  - online social media validator
  - try social links
  - browser demo
  - test social platform URLs
  - validate URLs online
  - detect platform online
  - sanitize URLs online
---

# Interactive Demo

Try the `social-links` library directly in your browser! This page uses [Pyodide](https://pyodide.org/) to run Python in the browser.

<div id="pyodide-loading" style="text-align: center; padding: 40px 20px;">
  <div class="spinner"></div>
  <p style="margin-top: 15px; color: #666;">Loading Pyodide...</p>
</div>

<div id="playground-container" style="display: none;">
  <!-- Package Info Banner -->
  <div id="package-info" style="display: none; margin-bottom: 20px; padding: 12px 16px; background: #e3f2fd; border-left: 4px solid #1976d2; border-radius: 4px;">
    <span style="font-weight: 500;">Installed:</span> <code>social-links</code> <span id="package-version" style="font-weight: 600; color: #1976d2;"></span>
    <span style="margin-left: 20px; color: #666;">•</span>
    <span style="margin-left: 10px; font-weight: 500;">Platforms:</span> <span id="platform-count" style="font-weight: 600; color: #1976d2;"></span>
  </div>

  <!-- Main Layout -->
  <div class="playground-layout">
    <!-- URL Input Panel -->
    <div class="url-panel">
      <div class="panel-header">
        <span class="panel-title">Test URL</span>
        <div class="example-buttons">
          <button class="example-btn active" data-example="linkedin">LinkedIn</button>
          <button class="example-btn" data-example="github">GitHub</button>
          <button class="example-btn" data-example="twitter">X/Twitter</button>
          <button class="example-btn" data-example="instagram">Instagram</button>
          <button class="example-btn" data-example="custom">Custom</button>
        </div>
      </div>

      <div class="url-input-container">
        <input
          type="text"
          id="url-input"
          class="url-input"
          placeholder="Enter a social media URL to test..."
          spellcheck="false"
        />
        <div class="url-hint">Try: https://linkedin.com/in/username or just paste any social URL</div>
      </div>

      <!-- Quick Stats -->
      <div class="stats-bar">
        <div class="stat-item">
          <span class="stat-label">Detected</span>
          <span class="stat-value" id="stat-platform">-</span>
        </div>
        <div class="stat-item">
          <span class="stat-label">Valid</span>
          <span class="stat-value" id="stat-valid">-</span>
        </div>
      </div>
    </div>

    <!-- Operations Panel -->
    <div class="ops-panel">
      <div class="ops-tabs">
        <button class="ops-tab active" data-op="detect">detect_platform</button>
        <button class="ops-tab" data-op="validate">is_valid</button>
        <button class="ops-tab" data-op="sanitize">sanitize</button>
        <button class="ops-tab" data-op="platforms">list_platforms</button>
      </div>

      <div class="ops-content">
        <!-- Detect Platform Section -->
        <div class="op-section active" data-op="detect">
          <h3 class="op-title">Detect Platform</h3>
          <p class="op-description">Automatically detect which social media platform a URL belongs to.</p>

          <div class="form-group">
            <label class="form-label">URL</label>
            <input type="text" id="detect-url" class="form-input" placeholder="https://linkedin.com/in/username" />
            <p class="form-hint">Enter any social media URL</p>
          </div>

          <button id="detect-btn" class="execute-btn">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="5 3 19 12 5 21 5 3"></polygon></svg>
            Execute
          </button>

          <div class="code-preview">
            <div class="code-preview-header">
              <span>Python Code</span>
              <button class="copy-btn" onclick="copyCode('detect')">Copy</button>
            </div>
            <div class="code-preview-body" id="detect-code-preview">
              <span class="code-fn">detect_platform</span>(<span class="code-str">"url"</span>)
            </div>
          </div>

          <div id="detect-result" class="result-panel"></div>
        </div>

        <!-- Validate URL Section -->
        <div class="op-section" data-op="validate">
          <h3 class="op-title">Validate URL</h3>
          <p class="op-description">Check if a URL is valid for a specific social media platform.</p>

          <div class="form-group">
            <label class="form-label">Platform</label>
            <select id="validate-platform" class="form-select">
              <option value="">Select platform...</option>
            </select>
          </div>

          <div class="form-group">
            <label class="form-label">URL</label>
            <input type="text" id="validate-url" class="form-input" placeholder="https://linkedin.com/in/username" />
            <p class="form-hint">Enter a URL to validate</p>
          </div>

          <button id="validate-btn" class="execute-btn">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="5 3 19 12 5 21 5 3"></polygon></svg>
            Execute
          </button>

          <div class="code-preview">
            <div class="code-preview-header">
              <span>Python Code</span>
              <button class="copy-btn" onclick="copyCode('validate')">Copy</button>
            </div>
            <div class="code-preview-body" id="validate-code-preview">
              <span class="code-fn">is_valid</span>(<span class="code-str">"platform"</span>, <span class="code-str">"url"</span>)
            </div>
          </div>

          <div id="validate-result" class="result-panel"></div>
        </div>

        <!-- Sanitize URL Section -->
        <div class="op-section" data-op="sanitize">
          <h3 class="op-title">Sanitize URL</h3>
          <p class="op-description">Normalize a URL to its canonical format by removing extra parameters and standardizing the structure.</p>

          <div class="form-group">
            <label class="form-label">Platform</label>
            <select id="sanitize-platform" class="form-select">
              <option value="">Select platform...</option>
            </select>
          </div>

          <div class="form-group">
            <label class="form-label">URL</label>
            <input type="text" id="sanitize-url" class="form-input" placeholder="https://www.linkedin.com/in/username/" />
            <p class="form-hint">Enter a URL to normalize</p>
          </div>

          <button id="sanitize-btn" class="execute-btn">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="5 3 19 12 5 21 5 3"></polygon></svg>
            Execute
          </button>

          <div class="code-preview">
            <div class="code-preview-header">
              <span>Python Code</span>
              <button class="copy-btn" onclick="copyCode('sanitize')">Copy</button>
            </div>
            <div class="code-preview-body" id="sanitize-code-preview">
              <span class="code-fn">sanitize</span>(<span class="code-str">"platform"</span>, <span class="code-str">"url"</span>)
            </div>
          </div>

          <div id="sanitize-result" class="result-panel"></div>
        </div>

        <!-- List Platforms Section -->
        <div class="op-section" data-op="platforms">
          <h3 class="op-title">Supported Platforms</h3>
          <p class="op-description">View all 65+ supported social media platforms with built-in validation rules.</p>

          <button id="platforms-btn" class="execute-btn">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="5 3 19 12 5 21 5 3"></polygon></svg>
            Show All Platforms
          </button>

          <div class="code-preview">
            <div class="code-preview-header">
              <span>Python Code</span>
              <button class="copy-btn" onclick="copyCode('platforms')">Copy</button>
            </div>
            <div class="code-preview-body">
              <span class="code-fn">list_platforms</span>()
            </div>
          </div>

          <div id="platforms-result" class="result-panel"></div>
        </div>
      </div>
    </div>
  </div>
</div>

<style>
  /* Spinner */
  .spinner {
    border: 4px solid #e0e0e0;
    border-top: 4px solid #1976d2;
    border-radius: 50%;
    width: 40px;
    height: 40px;
    animation: spin 1s linear infinite;
    margin: 0 auto;
  }

  @keyframes spin {
    0% { transform: rotate(0deg); }
    100% { transform: rotate(360deg); }
  }

  /* Main Layout */
  .playground-layout {
    display: flex;
    flex-direction: column;
    gap: 20px;
  }

  /* URL Input Panel */
  .url-panel {
    background: #263238;
    border-radius: 8px;
    display: flex;
    flex-direction: column;
    overflow: hidden;
  }

  .panel-header {
    padding: 12px 16px;
    background: #1e272c;
    display: flex;
    justify-content: space-between;
    align-items: center;
    flex-wrap: wrap;
    gap: 10px;
  }

  .panel-title {
    font-weight: 600;
    font-size: 0.85rem;
    text-transform: uppercase;
    letter-spacing: 0.5px;
    color: #90a4ae;
  }

  .example-buttons {
    display: flex;
    gap: 6px;
    flex-wrap: wrap;
  }

  .example-btn {
    padding: 5px 10px;
    background: transparent;
    border: 1px solid #455a64;
    color: #b0bec5;
    border-radius: 4px;
    cursor: pointer;
    font-size: 0.75rem;
    transition: all 0.2s;
  }

  .example-btn:hover {
    background: #37474f;
    border-color: #607d8b;
  }

  .example-btn.active {
    background: #1976d2;
    color: white;
    border-color: #1976d2;
  }

  /* URL Input */
  .url-input-container {
    padding: 20px;
    background: #263238;
  }

  .url-input {
    width: 100%;
    padding: 14px 16px;
    background: #1e272c;
    border: 2px solid #37474f;
    color: #eceff1;
    font-family: 'Monaco', 'Menlo', 'Ubuntu Mono', monospace;
    font-size: 0.95rem;
    border-radius: 6px;
    outline: none;
    transition: border-color 0.2s;
  }

  .url-input:focus {
    border-color: #1976d2;
  }

  .url-input::placeholder {
    color: #546e7a;
  }

  .url-hint {
    margin-top: 10px;
    font-size: 0.75rem;
    color: #78909c;
  }

  /* Stats Bar */
  .stats-bar {
    padding: 10px 16px;
    background: #1e272c;
    display: flex;
    gap: 20px;
    border-top: 1px solid #37474f;
  }

  .stat-item {
    display: flex;
    align-items: center;
    gap: 8px;
  }

  .stat-label {
    font-size: 0.7rem;
    color: #78909c;
    text-transform: uppercase;
    letter-spacing: 0.5px;
  }

  .stat-value {
    background: #37474f;
    padding: 2px 10px;
    border-radius: 4px;
    color: #80cbc4;
    font-weight: 600;
    font-size: 0.8rem;
    font-family: monospace;
  }

  /* Operations Panel */
  .ops-panel {
    background: white;
    border-radius: 8px;
    border: 1px solid #e0e0e0;
    display: flex;
    flex-direction: column;
    overflow: hidden;
  }

  .ops-tabs {
    display: flex;
    background: #fafafa;
    border-bottom: 1px solid #e0e0e0;
    overflow-x: auto;
    flex-shrink: 0;
  }

  .ops-tab {
    padding: 12px 16px;
    background: transparent;
    border: none;
    color: #757575;
    cursor: pointer;
    font-size: 0.8rem;
    font-weight: 500;
    font-family: 'Monaco', 'Menlo', monospace;
    border-bottom: 2px solid transparent;
    white-space: nowrap;
    transition: all 0.2s;
  }

  .ops-tab:hover {
    color: #424242;
    background: #f5f5f5;
  }

  .ops-tab.active {
    color: #1976d2;
    border-bottom-color: #1976d2;
    background: white;
  }

  .ops-content {
    flex: 1;
    overflow: auto;
    padding: 20px;
  }

  .op-section {
    display: none;
  }

  .op-section.active {
    display: block;
  }

  .op-title {
    font-size: 1.1rem;
    font-weight: 600;
    margin: 0 0 6px 0;
    color: #212121;
  }

  .op-description {
    color: #757575;
    font-size: 0.9rem;
    margin: 0 0 20px 0;
  }

  /* Form Elements */
  .form-group {
    margin-bottom: 16px;
  }

  .form-label {
    display: block;
    font-size: 0.75rem;
    font-weight: 600;
    color: #616161;
    margin-bottom: 6px;
    text-transform: uppercase;
    letter-spacing: 0.5px;
  }

  .form-input, .form-select {
    width: 100%;
    padding: 10px 12px;
    border: 1px solid #e0e0e0;
    border-radius: 6px;
    font-size: 0.9rem;
    font-family: 'Monaco', 'Menlo', monospace;
    transition: border-color 0.2s, box-shadow 0.2s;
    background: white;
  }

  .form-select {
    cursor: pointer;
  }

  .form-input:focus, .form-select:focus {
    outline: none;
    border-color: #1976d2;
    box-shadow: 0 0 0 3px rgba(25, 118, 210, 0.1);
  }

  .form-input::placeholder {
    color: #bdbdbd;
  }

  .form-hint {
    font-size: 0.75rem;
    color: #9e9e9e;
    margin: 6px 0 0 0;
  }

  /* Execute Button */
  .execute-btn {
    width: 100%;
    padding: 12px 16px;
    background: #1976d2;
    color: white;
    border: none;
    border-radius: 6px;
    font-size: 0.9rem;
    font-weight: 600;
    cursor: pointer;
    transition: background 0.2s, transform 0.1s;
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 8px;
  }

  .execute-btn:hover {
    background: #1565c0;
  }

  .execute-btn:active {
    transform: scale(0.98);
  }

  /* Code Preview */
  .code-preview {
    margin-top: 16px;
    background: #263238;
    border-radius: 6px;
    overflow: hidden;
  }

  .code-preview-header {
    padding: 8px 12px;
    background: #1e272c;
    color: #90a4ae;
    font-size: 0.7rem;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 0.5px;
    display: flex;
    justify-content: space-between;
    align-items: center;
  }

  .copy-btn {
    padding: 3px 8px;
    background: #37474f;
    border: none;
    color: #b0bec5;
    border-radius: 3px;
    cursor: pointer;
    font-size: 0.65rem;
    text-transform: uppercase;
  }

  .copy-btn:hover {
    background: #455a64;
  }

  .code-preview-body {
    padding: 12px;
    font-family: 'Monaco', 'Menlo', monospace;
    font-size: 0.85rem;
    color: #eceff1;
    overflow-x: auto;
  }

  .code-fn {
    color: #82aaff;
  }

  .code-str {
    color: #c3e88d;
  }

  /* Result Panel */
  .result-panel {
    margin-top: 16px;
    border-radius: 6px;
    overflow: hidden;
    border: 1px solid #e0e0e0;
    min-height: 50px;
  }

  .result-panel:empty {
    display: none;
  }

  .result-panel .result-header {
    padding: 8px 12px;
    background: #fafafa;
    font-size: 0.7rem;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 0.5px;
    color: #757575;
    display: flex;
    justify-content: space-between;
    align-items: center;
  }

  .result-panel .result-body {
    padding: 12px;
    font-family: 'Monaco', 'Menlo', monospace;
    font-size: 0.85rem;
    background: white;
  }

  .result-success {
    color: #2e7d32;
  }

  .result-error {
    color: #c62828;
  }

  .result-info {
    color: #1976d2;
  }

  .result-value {
    background: #f5f5f5;
    padding: 8px 12px;
    border-radius: 4px;
    margin-top: 8px;
    display: block;
    word-break: break-all;
  }

  .result-status {
    padding: 3px 8px;
    border-radius: 12px;
    font-size: 0.65rem;
    font-weight: 600;
  }

  .result-status.success {
    background: #e8f5e9;
    color: #2e7d32;
  }

  .result-status.error {
    background: #ffebee;
    color: #c62828;
  }

  .platforms-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(140px, 1fr));
    gap: 8px;
    margin-top: 12px;
  }

  .platform-badge {
    background: #f5f5f5;
    padding: 8px 12px;
    border-radius: 4px;
    font-size: 0.8rem;
    text-align: center;
    font-family: monospace;
    color: #424242;
  }

  /* Responsive */
  @media (max-width: 768px) {
    .ops-tab {
      padding: 10px 12px;
      font-size: 0.75rem;
    }

    .panel-header {
      flex-direction: column;
      align-items: flex-start;
    }

    .example-buttons {
      width: 100%;
    }

    .platforms-grid {
      grid-template-columns: repeat(auto-fill, minmax(100px, 1fr));
    }
  }
</style>

<script src="https://cdn.jsdelivr.net/pyodide/v0.24.1/full/pyodide.js"></script>

<script type="text/javascript">
  let pyodide;
  let currentUrl = "";
  let currentCodeStrings = {};
  const EXAMPLE_URLS = {
    linkedin: "https://www.linkedin.com/in/ysskrishna/",
    github: "https://github.com/ysskrishna",
    twitter: "https://x.com/ysskrishna",
    instagram: "https://instagram.com/ysskrishna",
    custom: ""
  };

  async function main() {
    // Load Pyodide
    pyodide = await loadPyodide({
      indexURL: "https://cdn.jsdelivr.net/pyodide/v0.24.1/full/"
    });

    // Update loading message
    document.getElementById("pyodide-loading").innerHTML = '<div class="spinner"></div><p style="margin-top: 15px; color: #666;">Installing social-links package...</p>';

    // Install social-links package
    await pyodide.loadPackage("micropip");
    const micropip = pyodide.pyimport("micropip");
    await micropip.install("social-links");

    // Import and initialize
    pyodide.runPython(`
      from sociallinks import detect_platform, is_valid, sanitize, list_platforms
      
      # Try to get package version
      try:
          import importlib.metadata
          package_version = importlib.metadata.version('social-links')
      except:
          try:
              import importlib_metadata
              package_version = importlib_metadata.version('social-links')
          except:
              package_version = "unknown"
    `);

    const packageVersion = pyodide.globals.get("package_version");

    // Display package version
    if (packageVersion && packageVersion !== "unknown") {
      document.getElementById("package-version").textContent = `v${packageVersion}`;
    }

    // Get platform count
    const platformsList = pyodide.runPython("list_platforms()").toJs();
    document.getElementById("platform-count").textContent = platformsList.length;
    document.getElementById("package-info").style.display = "block";

    // Hide loading, show interface
    document.getElementById("pyodide-loading").style.display = "none";
    document.getElementById("playground-container").style.display = "block";

    // Load default example
    loadExample("linkedin");

    // Populate platform dropdowns
    populatePlatformDropdowns(platformsList);

    // Setup event listeners
    setupEventListeners();
  }

  function loadExample(exampleType) {
    const url = EXAMPLE_URLS[exampleType] || "";
    document.getElementById("url-input").value = url;
    currentUrl = url;
    
    // Update example buttons
    document.querySelectorAll('.example-btn').forEach(btn => btn.classList.remove('active'));
    document.querySelector(`.example-btn[data-example="${exampleType}"]`).classList.add('active');

    // Auto-update stats if URL is provided
    if (url) {
      updateQuickStats(url);
    } else {
      resetQuickStats();
    }

    // Clear results
    clearResults();
  }

  function populatePlatformDropdowns(platformsList) {
    const sorted = platformsList.sort();
    
    const validateSelect = document.getElementById("validate-platform");
    const sanitizeSelect = document.getElementById("sanitize-platform");
    
    sorted.forEach(platform => {
      const option1 = document.createElement("option");
      option1.value = platform;
      option1.textContent = platform;
      validateSelect.appendChild(option1);
      
      const option2 = document.createElement("option");
      option2.value = platform;
      option2.textContent = platform;
      sanitizeSelect.appendChild(option2);
    });
  }

  function updateQuickStats(url) {
    try {
      const platform = pyodide.runPython(`detect_platform(${JSON.stringify(url)})`);
      document.getElementById("stat-platform").textContent = platform || "none";
      
      if (platform) {
        const valid = pyodide.runPython(`is_valid(${JSON.stringify(platform)}, ${JSON.stringify(url)})`);
        document.getElementById("stat-valid").textContent = valid ? "✓" : "✗";
      } else {
        document.getElementById("stat-valid").textContent = "-";
      }
    } catch (e) {
      resetQuickStats();
    }
  }

  function resetQuickStats() {
    document.getElementById("stat-platform").textContent = "-";
    document.getElementById("stat-valid").textContent = "-";
  }

  function setupEventListeners() {
    // Example buttons
    document.querySelectorAll('.example-btn').forEach(btn => {
      btn.addEventListener('click', () => {
        loadExample(btn.dataset.example);
      });
    });

    // Operation tabs
    document.querySelectorAll('.ops-tab').forEach(tab => {
      tab.addEventListener('click', () => {
        document.querySelectorAll('.ops-tab').forEach(t => t.classList.remove('active'));
        document.querySelectorAll('.op-section').forEach(s => s.classList.remove('active'));

        tab.classList.add('active');
        document.querySelector(`.op-section[data-op="${tab.dataset.op}"]`).classList.add('active');
      });
    });

    // URL input auto-update stats
    document.getElementById("url-input").addEventListener("input", (e) => {
      const url = e.target.value.trim();
      currentUrl = url;
      if (url) {
        updateQuickStats(url);
        // Update all operation fields
        document.getElementById("detect-url").value = url;
        document.getElementById("validate-url").value = url;
        document.getElementById("sanitize-url").value = url;
        updateDetectCodePreview();
        updateValidateCodePreview();
        updateSanitizeCodePreview();
      } else {
        resetQuickStats();
      }
    });

    // Update code previews on input
    document.getElementById("detect-url").addEventListener("input", updateDetectCodePreview);
    document.getElementById("validate-platform").addEventListener("change", updateValidateCodePreview);
    document.getElementById("validate-url").addEventListener("input", updateValidateCodePreview);
    document.getElementById("sanitize-platform").addEventListener("change", updateSanitizeCodePreview);
    document.getElementById("sanitize-url").addEventListener("input", updateSanitizeCodePreview);

    // Detect platform
    document.getElementById("detect-btn").addEventListener("click", () => {
      const url = document.getElementById("detect-url").value.trim();
      const resultDiv = document.getElementById("detect-result");

      if (!url) {
        showResult(resultDiv, "error", "Please enter a URL");
        return;
      }

      try {
        showResult(resultDiv, "info", "Processing...");
        const platform = pyodide.runPython(`detect_platform(${JSON.stringify(url)})`);
        
        if (platform) {
          showResult(resultDiv, "success", "Platform detected", platform);
        } else {
          showResult(resultDiv, "info", "No platform detected", "None");
        }
      } catch (error) {
        showResult(resultDiv, "error", error.message);
      }
    });

    // Validate URL
    document.getElementById("validate-btn").addEventListener("click", () => {
      const platform = document.getElementById("validate-platform").value;
      const url = document.getElementById("validate-url").value.trim();
      const resultDiv = document.getElementById("validate-result");

      if (!platform || !url) {
        showResult(resultDiv, "error", "Please select a platform and enter a URL");
        return;
      }

      try {
        showResult(resultDiv, "info", "Processing...");
        const valid = pyodide.runPython(`is_valid(${JSON.stringify(platform)}, ${JSON.stringify(url)})`);
        
        if (valid) {
          showResult(resultDiv, "success", `Valid ${platform} URL`, "True");
        } else {
          showResult(resultDiv, "error", `Invalid ${platform} URL`, "False");
        }
      } catch (error) {
        showResult(resultDiv, "error", error.message);
      }
    });

    // Sanitize URL
    document.getElementById("sanitize-btn").addEventListener("click", () => {
      const platform = document.getElementById("sanitize-platform").value;
      const url = document.getElementById("sanitize-url").value.trim();
      const resultDiv = document.getElementById("sanitize-result");

      if (!platform || !url) {
        showResult(resultDiv, "error", "Please select a platform and enter a URL");
        return;
      }

      try {
        showResult(resultDiv, "info", "Processing...");
        const sanitized = pyodide.runPython(`sanitize(${JSON.stringify(platform)}, ${JSON.stringify(url)})`);
        showResult(resultDiv, "success", "Sanitized URL", sanitized);
      } catch (error) {
        showResult(resultDiv, "error", error.message);
      }
    });

    // List platforms
    document.getElementById("platforms-btn").addEventListener("click", () => {
      const resultDiv = document.getElementById("platforms-result");

      try {
        showResult(resultDiv, "info", "Processing...");
        const platformsList = pyodide.runPython("list_platforms()").toJs();
        showResultPlatforms(resultDiv, platformsList.sort());
      } catch (error) {
        showResult(resultDiv, "error", error.message);
      }
    });

    // Enter key handlers
    ["detect-url", "validate-url", "sanitize-url"].forEach(id => {
      document.getElementById(id).addEventListener("keypress", (e) => {
        if (e.key === "Enter") {
          document.getElementById(id.replace("-url", "-btn")).click();
        }
      });
    });
  }

  function updateDetectCodePreview() {
    const url = document.getElementById("detect-url").value.trim() || "url";
    document.getElementById("detect-code-preview").innerHTML = 
      `<span class="code-fn">detect_platform</span>(<span class="code-str">"${escapeHtml(url)}"</span>)`;
  }

  function updateValidateCodePreview() {
    const platform = document.getElementById("validate-platform").value || "platform";
    const url = document.getElementById("validate-url").value.trim() || "url";
    document.getElementById("validate-code-preview").innerHTML = 
      `<span class="code-fn">is_valid</span>(<span class="code-str">"${escapeHtml(platform)}"</span>, <span class="code-str">"${escapeHtml(url)}"</span>)`;
  }

  function updateSanitizeCodePreview() {
    const platform = document.getElementById("sanitize-platform").value || "platform";
    const url = document.getElementById("sanitize-url").value.trim() || "url";
    document.getElementById("sanitize-code-preview").innerHTML = 
      `<span class="code-fn">sanitize</span>(<span class="code-str">"${escapeHtml(platform)}"</span>, <span class="code-str">"${escapeHtml(url)}"</span>)`;
  }

  function showResult(div, type, message, value = null) {
    const statusClass = type === "success" ? "success" : type === "error" ? "error" : "";
    const statusText = type === "success" ? "Success" : type === "error" ? "Error" : "Info";

    let html = `
      <div class="result-header">
        <span>Result</span>
        ${statusClass ? `<span class="result-status ${statusClass}">${statusText}</span>` : ''}
      </div>
      <div class="result-body">
        <span class="result-${type}">${escapeHtml(message)}</span>
        ${value ? `<code class="result-value">${escapeHtml(value)}</code>` : ''}
      </div>
    `;
    div.innerHTML = html;
  }

  function showResultPlatforms(div, platforms) {
    const platformsHtml = platforms.map(p => `<div class="platform-badge">${escapeHtml(p)}</div>`).join('');
    div.innerHTML = `
      <div class="result-header">
        <span>Result</span>
        <span class="result-status success">Success</span>
      </div>
      <div class="result-body">
        <span class="result-success">Found ${platforms.length} supported platforms:</span>
        <div class="platforms-grid">${platformsHtml}</div>
      </div>
    `;
  }

  function copyCode(op) {
    let code = '';
    switch(op) {
      case 'detect':
        const detectUrl = document.getElementById("detect-url").value.trim() || "url";
        code = `detect_platform("${detectUrl}")`;
        break;
      case 'validate':
        const validatePlatform = document.getElementById("validate-platform").value || "platform";
        const validateUrl = document.getElementById("validate-url").value.trim() || "url";
        code = `is_valid("${validatePlatform}", "${validateUrl}")`;
        break;
      case 'sanitize':
        const sanitizePlatform = document.getElementById("sanitize-platform").value || "platform";
        const sanitizeUrl = document.getElementById("sanitize-url").value.trim() || "url";
        code = `sanitize("${sanitizePlatform}", "${sanitizeUrl}")`;
        break;
      case 'platforms':
        code = 'list_platforms()';
        break;
    }

    navigator.clipboard.writeText(code).then(() => {
      const btn = event.target;
      const original = btn.textContent;
      btn.textContent = 'Copied!';
      setTimeout(() => btn.textContent = original, 1500);
    });
  }

  function clearResults() {
    document.querySelectorAll('.result-panel').forEach(el => el.innerHTML = '');
  }

  function escapeHtml(text) {
    const div = document.createElement("div");
    div.textContent = text;
    return div.innerHTML;
  }

  // Start loading Pyodide
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', () => {
      main().catch(err => {
        document.getElementById("pyodide-loading").innerHTML =
          `<p style="color: #c62828;">Error loading Pyodide: ${err.message}</p>`;
        console.error(err);
      });
    });
  } else {
    main().catch(err => {
      document.getElementById("pyodide-loading").innerHTML =
        `<p style="color: #c62828;">Error loading Pyodide: ${err.message}</p>`;
      console.error(err);
    });
  }
</script>

