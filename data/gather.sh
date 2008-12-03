#!/bin/zsh
for i in "mid" "top" "bot"
  ruby gather_data.rb $1$i
