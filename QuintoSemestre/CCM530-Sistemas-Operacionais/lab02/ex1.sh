echo "Digite a sua linguagem de programação"

if [ $1 == "python" ]; then
	./template_python.sh > $2
elif [ $1 == "java" ]; then 
	./template_java.sh > $2 
elif [ $1 == "c" ]; then
	./template_c.sh > $2
fi


echo "Linguagem selecionada "$1""
