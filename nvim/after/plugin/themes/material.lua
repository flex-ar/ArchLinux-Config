-- Material config
if (colorTheme ~= 'material') then return end

local status, material = pcall(require, 'material')
if (not status) then return end

material.setup({})

vim.g.material_style = 'oceanic'

vim.cmd 'colorscheme material'
