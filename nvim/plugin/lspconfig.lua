local status, lspconfig = pcall(require, "lspconfig")
if (not status) then return end

local ok, lsp_signature = pcall(require, "lsp_signature")
if (not ok) then return end

lsp_signature.setup({
  doc_lines = 0,
  toggle_key = '<C-q>'
})

local capabilities = vim.lsp.protocol.make_client_capabilities()
capabilities.textDocument.completion.completionItem.snippetSupport = true

lspconfig.tsserver.setup({
  cmd = { "typescript-language-server", "--stdio" },
  filetype = { "javascript", "javascriptreact", "javascript.jsx", "typescript", "typescriptreact", "typescript.tsx" },
  capabilities = capabilities,
})

lspconfig.eslint.setup({
  cmd = { "vscode-eslint-language-server", "--stdio" },
  filetype = { "javascript", "javascriptreact", "javascript.jsx", "typescript", "typescriptreact", "typescript.tsx", "vue" },
  settings = { packageManager = "yarn" },
})

lspconfig.html.setup({
  cmd = { "vscode-html-language-server", "--stdio" },
  filetype = { "html" },
  init_options = {
    configurationSection = { "html", "css", "javascript" },
    embeddedLanguages = { css = true, javascript = true, },
    provideFormatter = true,
  },
  single_file_support = true,
  capabilities = capabilities,
})

lspconfig.cssls.setup({
  cmd = { "vscode-css-language-server", "--stdio" },
  filetype = { "css", "scss" },
  settings = {
    css = { validate = true },
    scss = { validate = true },
  },
  single_file_support = true,
  capabilities = capabilities,
})

