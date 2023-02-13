local status, saga = pcall(require, "lspsaga")
if (not status) then return end

saga.setup({
  finder_icons = {
    def = '  ',
    ref = '  ',
    imp = '  ',
  },
  finder_action_keys = {
    open = "o",
    vsplit = "s",
    split = "i",
    tabe = "t",
    quit = "q",
  },
  server_filetype_map = {
    typescript = 'typescript',
  }
})

keymap('n', 'gd', '<Cmd>Lspsaga lsp_finder<CR>')
keymap({'n','v'}, '<leader>ca', '<cmd>Lspsaga code_action<CR>')
keymap('n', 'gr', '<Cmd>Lspsaga rename<CR>')
keymap('n', 'gp', '<Cmd>Lspsaga peek_definition<CR>')
keymap('n', 'K', '<Cmd>Lspsaga hover_doc<CR>')
keymap('n', '<C-j>', '<Cmd>Lspsaga diagnostic_jump_next<CR>')


-- funcion removida de lspsaga
-- keymap('i', '<C-k>', '<Cmd>Lspsaga signature_help<CR>')

