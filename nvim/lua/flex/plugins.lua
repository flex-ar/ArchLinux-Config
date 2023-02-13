vim.cmd([[packadd packer.nvim]])

return require('packer').startup(function(use)
  use 'wbthomason/packer.nvim'
  use 'lewis6991/impatient.nvim'
 
  use 'glepnir/dashboard-nvim'

  -- Configurations for Nvim LSP
  use 'neovim/nvim-lspconfig'
  use {
    'glepnir/lspsaga.nvim', -- LSP UIs
    branch = 'main'
  }

  -- Completition
  use 'onsails/lspkind-nvim' -- vscode-like pictograms
  use 'hrsh7th/cmp-buffer' -- nvim-cmp source for buffer words
  use 'hrsh7th/cmp-nvim-lsp' -- nvim-cmp source for neovim's built-in LSP
  use 'hrsh7th/nvim-cmp' -- Completion
  use 'ray-x/lsp_signature.nvim' -- To obtain the signature of the function we use

  -- Snippets
  use 'L3MON4D3/LuaSnip'
  use 'saadparwaiz1/cmp_luasnip'
  use 'rafamadriz/friendly-snippets'

  -- Formatting
  use 'jose-elias-alvarez/null-ls.nvim' -- Use Neovim as a language server to inject LSP diagnostics, code actions, and more via Lua

  -- Comment
  use 'numToStr/Comment.nvim'

  -- Git
  use 'lewis6991/gitsigns.nvim'

  -- Syntax highlightings
  use { 
    'nvim-treesitter/nvim-treesitter',
    run = ':TSUpdate',
    requires = {
      'p00f/nvim-ts-rainbow',
      'windwp/nvim-ts-autotag',
    },
  }

  -- telescope
  use 'nvim-lua/plenary.nvim'
  use 'nvim-telescope/telescope.nvim'
  use 'nvim-telescope/telescope-file-browser.nvim'
  use 'kyazdani42/nvim-web-devicons' -- File icons

  -- indent colorized
  use 'lukas-reineke/indent-blankline.nvim'

  -- Autopairs
  use 'windwp/nvim-autopairs'

  -- Colors Hex
  use 'norcalli/nvim-colorizer.lua'

  -- Theme
  use 'folke/tokyonight.nvim'
  use { 'rose-pine/neovim', as = 'rose-pine', tag = 'v1.*', }
  use 'marko-cerovac/material.nvim'

  -- Tab style
  use 'akinsho/nvim-bufferline.lua'

  -- Status line
  use 'nvim-lualine/lualine.nvim'

end)
