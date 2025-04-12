#!/bin/bash

reserved_path=$(pwd)
cd /home/brian/MY_TEST/Chat
source ../.global


declare exe_file="./menu.sh"
if [ -z "$1" ];then
	exec $exe_file
fi

case "$1" in
	'-h' | '--help')
		echo -e "\n(self-defined) CHAT, version $CHAT_version\n"
		echo -e "Usage: chat with online or offline LLM [arguments]\nOptions:"
		echo -e "  -h, --help\t\tdisplay this message"
		echo -e "  -v, --version\t\tdisplay version"
		echo -e "  -l, --list\t\tlist avaliable offline models(based ollama)"
		;;


	'-v' | '--version')
		echo -e "CHAT script v$CHAT_version"
		;;


	'-l' | '--list')
		content=$(python3 -c "import globl; print(' '.join(globl.model_options))")
		echo -e "offline models:\n\t$content"	
		;;
	

	*)
		unrecognized_option "chat" $1
		;;
esac

cd $reserved_path
