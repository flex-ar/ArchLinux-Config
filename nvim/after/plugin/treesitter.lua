local status, ts = pcall(require, "nvim-treesitter.configs")
if (not status) then return end

-- if (colorTheme == 'tykyonight') then
--   vim.cmd([[ autocmd FileType * highlight rainbowcol1 guifg=#7AA2F7 ]])
-- end

ts.setup {
  highlight = {
    enable = true,
    disable = {},
  },
  indent = {
    enable = true,
    disable = {},
  },
  ensure_installed = {
    "rust",
    "python",
    "javascript",
    "typescript",
    "sql",
    "haskell",
    "tsx",
    "toml",
    "fish",
    "json",
    "yaml",
    "css",
    "scss",
    "html",
    "lua",
    "glimmer",
  },
  autotag = {
    enable = true,
  },
  rainbow = {
    enable = true,
    extended_mode = false,
    max_file_line = nil,
  }
}

local parser_config = require "nvim-treesitter.parsers".get_parser_configs()
parser_config.tsx.filetype_to_parsername = { "javascript", "typescript.tsx" }
