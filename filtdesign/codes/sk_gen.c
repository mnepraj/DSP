#include <stdio.h>
#include <math.h>
#include <complex.h>

#define N 4
#define EPSILON 0.3
#define OMEGA_LP 1
#define PI 3.14159265358979323846

int main() {
    // Calculate B_k coefficient
    double B_k = asinh(1 / EPSILON) / N;

    // Initialize an array to store the poles
    double complex poles[2*N];

    // Calculate poles
    for (int k = 0; k < 2*N; k++) {
        double A_k = (2*k + 1) * PI / (2*N);
        poles[k] = -OMEGA_LP * csin(A_k) * csinh(B_k) - I * OMEGA_LP * ccos(A_k) * ccosh(B_k);
    }

    // Save poles to a .dat file
    FILE *file = fopen("poles.txt", "w");
    if (file == NULL) {
        printf("Error opening file.\n");
        return 1;
    }
    fprintf(file, "Real Part, Imaginary Part\n");
    for (int i = 0; i < 2*N; ++i) {
        fprintf(file, "%.4f, %.4f\n", creal(poles[i]), cimag(poles[i]));
    }
    fclose(file);

    printf("Poles saved to poles.txt file.\n");

    return 0;
}
