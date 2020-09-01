# ejercicio 1. Escribir
echo "Hello World"

# ejercicio 2. Crear carpeta
mkdir new_dir

# ejercicio 3. Eliminar carpeta
rmdir new_dir

# ejercicio 4. Copiar txt de un file a otro
cp lorem/sed.txt lorem-copy

# ejercicio 5. Copia los otros 2 archivos a lorem-copy.
cp lorem/{at.txt,lorem.txt} lorem-copy/

# ejercicio 6. mostrar el contenido de sed.txt.
cat lorem-copy/sed.txt

# ejercicio 7.mostrar contenido de at.txt y lorem.txt.
cat lorem-copy/at.txt lorem.txt

# ejercicio 8.Visualiza las 3 primeras lineas.
cat lorem-copy/sed.txt|head -n 3

# ejercicio 9.Visualiza las 3 ultimas lineas.
cat lorem-copy/sed.txt|tail -n 3

# ejercicio 10.Añade al final de sed texto de lorem-copy.
echo " Homo homini lupus.">>lorem-copy/sed.txt

# ejercicio 11.Visualiza las 3 ultimas lineas de sed.
cat lorem-copy/sed.txt|tail -n 3

# ejercicio 12.Editar at.txt dentro de lorem-copy. Deberás usar sed.
sed 's/et/ET/g' lorem-copy/at.txt
# ejercicio 13.Encuentra al usuario activo en el sistema.
w 

# ejercicio 14.Encuentra dónde estás en tu sistema de ficheros.
pwd

# ejercicio 15.lista los archivos que terminan por .txt en la carpeta lorem.
cd lorem
ls -la
# ejercicio 16.número de líneas de sed.txt dentro de lorem.

# ejercicio 17. número de archivos que empiezan por lorem que están en  los directorios 
# ejercicio 18.Encuentra todas las apariciones de et en at.txt dentro de la carpeta lorem.
# ejercicio 19.número de apariciones del string et en at.txt dentro de la carpeta lorem..
# ejercicio 20.Cuenta el número de apariciones del string et en todos los archivos del directorio lorem-copy.
