local status, telescope = pcall(require, "telescope")
if (not status) then return end
local actions = require('telescope.actions')
local builtin = require("telescope.builtin")

local function telescope_buffer_dir()
  return vim.fn.expand('%:p:h')
end

local fb_actions = telescope.extensions.file_browser.actions

telescope.setup {
  defaults = {
    mappings = {
      n = {
        ["q"] = actions.close
      },
    },
    prompt_prefix = "   ",
    selection_caret = "🠶 ",
    layout_config = {
      prompt_position = "top",
      width = 0.8,
      height = 0.9,
      preview_cutoff = 120,
    },
    sorting_strategy = "ascending",
    file_ignore_patterns = { "node_modules", "dist" },
    set_env = { ["COLORTERM"] = "truecolor" },
  },
  extensions = {
    file_browser = {
      mappings = {
        -- your custom insert mode mappings
        ["i"] = {
          ["<C-w>"] = function() vim.cmd('normal vbd') end,
        },
        ["n"] = {
          -- your custom normal mode mappings
          ["N"] = fb_actions.create,
          ["h"] = fb_actions.goto_parent_dir,
          ["/"] = function()
            vim.cmd('startinsert')
          end
        },
      },
    },
  },
}

telescope.load_extension("file_browser")

keymap('n', ';gc', function() builtin.git_commits() end)

keymap('n', ';gb', function() builtin.git_branches() end)

keymap('n', ';gs', function() builtin.git_status() end)

keymap('n', ';f', function() builtin.find_files({ no_ignore = false, hidden = true }) end)

keymap('n', ';r', function() builtin.live_grep() end)

keymap('n', '\\\\', function() builtin.buffers() end)

keymap('n', ';t', function() builtin.help_tags() end)

keymap('n', ';;', function() builtin.resume() end)

keymap('n', ';e', function() builtin.diagnostics() end)

keymap("n", "sf", function()
  telescope.extensions.file_browser.file_browser({
    path = "%:p:h",
    cwd = telescope_buffer_dir(),
    respect_gitignore = false,
    hidden = true,
    grouped = true,
  })
end)
