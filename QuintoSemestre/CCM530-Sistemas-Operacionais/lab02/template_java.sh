if [ -z $1 ]; then
 class="Main"
else
 class=$1
fi

echo "public class ${class}{"
echo "public static void main(String[] args){"
echo "System.out.println(\"Hello World\");"
echo "}"
echo "}"
