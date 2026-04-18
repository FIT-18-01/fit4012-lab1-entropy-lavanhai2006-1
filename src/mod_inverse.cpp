#include <iostream>
using namespace std;

long long extended_euclid(long long a, long long b, long long &x, long long &y) {
    if (b == 0) {
        x = 1;
        y = 0;
        return a;
    }

    long long x1, y1;
    long long g = extended_euclid(b, a % b, x1, y1);

    x = y1;
    y = x1 - (a / b) * y1;

    return g;
}

int mod_inverse(int a, int m) {
    if (m <= 1) return -1;

    long long aa = a % m;
    if (aa < 0) aa += m;

    long long x, y;
    long long g = extended_euclid(aa, m, x, y);

    if (g != 1) return -1;

    return static_cast<int>((x % m + m) % m);
}

int main() {
    int a, m;
    cin >> a >> m;

    cout << mod_inverse(a, m) << endl;

    return 0;
}
