keymap = function(mode, lhs, rhs)
  vim.keymap.set(mode, lhs, rhs, { noremap = true, silent = true })
end

vim.g.mapleader = " "

keymap('n', '<leader>f', ':EslintFixAll<CR>')

-- Salir del modo insertar
keymap('i', 'kk', '<Esc>')

-- Seleccionar todo
keymap('n', '<C-a>', 'gg<S-v>G')

-- Tabular
keymap('v', '.', '>gv')
keymap('v', ',', '<gv')

-- New tab
keymap('n', 'te', ':tabnew<CR>')
-- Split window
keymap('n', 'ss', ':split<Return><C-w>w')
keymap('n', 'sv', ':vsplit<Return><C-w>w')
-- Move window
keymap('n', '<Space>', '<C-w>w')
keymap('', 'sh', '<C-w>h')
keymap('', 'sk', '<C-w>k')
keymap('', 'sj', '<C-w>j')
keymap('', 'sl', '<C-w>l')

-- Resize window
keymap('n', '<C-w><left>', '<C-w><')
keymap('n', '<C-w><right>', '<C-w>>')
keymap('n', '<C-w><up>', '<C-w>+')
keymap('n', '<C-w><down>', '<C-w>-')

-- nnoremap <C-s> :w<CR>
