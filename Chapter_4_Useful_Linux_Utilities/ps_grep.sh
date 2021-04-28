ps auxw | grep ping | grep -v grep

# use ps command with auxw and pipeline to filter ping processes

alias pg='ps aux | grep -v grep | grep $1' #take an argument from stdin
