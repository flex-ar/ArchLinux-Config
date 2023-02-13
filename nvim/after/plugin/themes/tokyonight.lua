-- Tokyonight config
if (colorTheme ~= 'tokyonight') then return end

local status, tokyonight = pcall(require, 'tokyonight')
if (not status) then return end

tokyonight.setup({
  style = "night",
  styles = {
    comments = { italic = true },
    keywords = { italic = true },
    sidebars = "dark",
    floats = "dark",
  }
})

vim.cmd 'colorscheme tokyonight'
