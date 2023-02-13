pcall(require, "impatient")

if require "flex.first_load"() then
  return
end

require("flex.globals")
require("flex.settings")
require("flex.keymaps")
require("flex.plugins")

