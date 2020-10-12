// Algoritmo_Genetico_fun.cpp : Este archivo contiene la función "main". La ejecución del programa comienza y termina ahí.
//

#include <iostream>
#include <vector>
#include <bitset>
#include <string>
#include <stdlib.h> 
#include <math.h> 
#include <time.h> 
using namespace std;

#define rand_start 1
#define rand_end 1000
#define n_pob 4
#define n_iter 100
#define len 10
#define l unsigned long

void seleccion(vector<string> &pob, vector<float>&fun, float media);
vector<string> cruzamiento(vector<string> &pob);
void mutacion(string &individuo1, string &individuo2);

l to_int(string n) {
	int x = bitset<len>(n).to_ulong();
	return x;
}

string to_binario(l x) {
	string res = "";
	res = bitset<len>(x).to_string();
	return res;
}

l get_random_number(int r1, int r2 = 0) {
	return rand() % r1 + r2;
}

l funcion(int x) {
	return pow(x, 2);
}
l funcion(int x, int exp) {
	return pow(x, exp);
}
void seleccion(vector<string> &pob, vector<float>&fun, float media) {
	vector<string> padres;
	//cout << "Valor Esperado:" << t << endl;
	//cout << "Valor Actual: " << rep << endl;
	int i = 0, j = 0;
	while (i < n_pob && j != n_pob) {
		const double rep = static_cast<int>(fun[j] / media * 1.0 + 0.5) / 1.0;
		for (int k = 0; k < rep; ++k) {
			padres.push_back(pob[j]);
		}
		i += rep;
		j++;
	}
	vector<string> nueva_generacion = cruzamiento(padres);
	pob = nueva_generacion;
}
vector<string> cruzamiento(vector<string> &pob) {
	vector<string> nueva_generacion;
	for (int i = 0; i < n_pob/2; i=i+2) {
		//int gen1 = get_random_number(pob.size());
		//int gen2 = get_random_number(pob.size());
		int r1 = i;
		int r2 = i + 1;
		//cout << "i:" << r1 << r2 << endl;
		//cout << "pob:" << pob[r1] << pob[r2] << endl;
		string c1 = pob[r1];
		string c2 = pob[r2];
		mutacion(c1, c2);
		nueva_generacion.push_back(c1);
		nueva_generacion.push_back(c2);
	}
	return nueva_generacion;
}
void mutacion(string &individuo1, string &individuo2) {
	int count = 10;
	int random_pos_mutation = rand() % individuo1.length();
	char g1 = individuo1[random_pos_mutation];
	char g2 = individuo2[random_pos_mutation];
	/*
	while (g1 == g2 && count>0) {
		//cout << "entra" << endl;
		random_pos_mutation = rand() % individuo1.length();
		g1 = individuo1[random_pos_mutation];
		g2 = individuo2[random_pos_mutation];
		count--;
	}
	*/
	char temp = individuo1[random_pos_mutation];
	individuo1[random_pos_mutation] = individuo2[random_pos_mutation];
	individuo2[random_pos_mutation] = temp;
}
void algoritmo_genetico(){
	srand(time(NULL));
	vector<string> poblacion;
	vector<float> fun_aptitud;
	l mejor_individuo = 0;
	float promedio_individuo = 0;
	for (int i = 0; i < n_pob; ++i) {
		l individuo1 = rand() % rand_end;
		poblacion.push_back(to_binario(individuo1));
		promedio_individuo += individuo1;
		//cout << "I:" << individuo1 << endl;
		if (individuo1 > mejor_individuo) {
			mejor_individuo = individuo1;
		}
	}
	promedio_individuo /= n_pob;
	//for (int i = 0; i < poblacion.size(); ++i) {
	//	l ind = to_int(poblacion[i]);
	//}
	
	float media = 0;
	for (int i = 0; i < n_iter; ++i) {
		for (int j = 0; j < n_pob; ++j) {
			l temp = funcion(to_int(poblacion[j]));
			//cout << "FUN:" << temp << endl;
			fun_aptitud.push_back(temp);
			media += temp;
		}
		media /= n_pob;
		seleccion(poblacion, fun_aptitud, media);
		cout << "MEJOR INDIVIDUO: " << mejor_individuo << endl;
		cout << "PROMEDIO" << promedio_individuo << endl;
	}
}
int main(){
	algoritmo_genetico();
    //cout << "Hello World!\n";
}

// Ejecutar programa: Ctrl + F5 o menú Depurar > Iniciar sin depurar
// Depurar programa: F5 o menú Depurar > Iniciar depuración

// Sugerencias para primeros pasos: 1. Use la ventana del Explorador de soluciones para agregar y administrar archivos
//   2. Use la ventana de Team Explorer para conectar con el control de código fuente
//   3. Use la ventana de salida para ver la salida de compilación y otros mensajes
//   4. Use la ventana Lista de errores para ver los errores
//   5. Vaya a Proyecto > Agregar nuevo elemento para crear nuevos archivos de código, o a Proyecto > Agregar elemento existente para agregar archivos de código existentes al proyecto
//   6. En el futuro, para volver a abrir este proyecto, vaya a Archivo > Abrir > Proyecto y seleccione el archivo .sln
