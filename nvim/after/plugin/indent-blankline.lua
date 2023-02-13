local status, indent_blankline = pcall(require, "indent_blankline")
if (not status) then return end

-- vim.opt.list = true
-- vim.opt.listchars:append "space:⋅"
-- vim.cmd [[highlight IndentBlanklineIndent1 guifg=#444b6a gui=nocombine]]

indent_blankline.setup({
  -- space_char_blankline = " ",
  -- show_current_context = true,
  -- show_current_context_start = true,
  -- char_highlight_list = {
  --   "IndentBlanklineIndent1",
  -- },
})
