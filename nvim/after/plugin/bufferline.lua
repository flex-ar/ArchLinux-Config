local status, bufferline = pcall(require, "bufferline")
if (not status) then return end

local highlightsTokyo = function ()
  if colorTheme == "tokyonight" then
    return {
      separator = {
        fg = '#000000',
        bg = '#000000',
      },
      background = {
        bg = '#100f16'
      }
    } 
  end
end

bufferline.setup({
  options = {
    mode = "tabs",
    diagnostics = "nvim_lsp",
    always_show_bufferline = false,
    show_buffer_close_icons = false,
    show_close_icon = false,
    color_icons = true
  },
  -- highlightsTokyo(),
  -- Tokyo Night
  -- highlights = {
  --   separator = {
  --     fg = '#000000',
  --     bg = '#000000',
  --   },
  --   background = {
  --     bg = '#100f16'
  --   }
  -- },
})

keymap('n', '<Tab>', '<Cmd>BufferLineCycleNext<CR>')
keymap('n', '<S-Tab>', '<Cmd>BufferLineCyclePrev<CR>')
