#include <stdio.h>

/* Herramienta interna: se supone que revisa el ultimo respaldo del sistema.
   Abre la ruta directamente con los privilegios efectivos del binario, sin
   comprobar quien lo esta ejecutando. Por eso cualquiera que lo corra con
   el bit SUID activo puede leer un archivo que su propio usuario no podria
   abrir por si mismo. */
int main(void) {
    FILE *archivo = fopen("/root/flag.txt", "r");
    if (!archivo) {
        perror("No se pudo abrir el respaldo");
        return 1;
    }

    char buffer[256];
    size_t leidos = fread(buffer, 1, sizeof(buffer) - 1, archivo);
    buffer[leidos] = '\0';
    fclose(archivo);

    printf("%s\n", buffer);
    return 0;
}
