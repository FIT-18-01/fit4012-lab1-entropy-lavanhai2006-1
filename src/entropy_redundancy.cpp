#include <cmath>
#include <iostream>
#include <map>
#include <string>
#include <iomanip>

using namespace std;

double calculate_entropy(const string &text) {
    if (text.empty()) return 0.0;

    map<char, int> freq;
    for (char c : text) {
        freq[c]++;
    }

    double entropy = 0.0;
    for (const auto &pair : freq) {
        double p = (double)pair.second / text.size();
        entropy -= p * log2(p);
    }

    return entropy;
}

double calculate_redundancy(const string &text, int alphabet_size = 256) {
    if (text.empty()) return 0.0;

    double max_entropy = log2(alphabet_size);
    double actual_entropy = calculate_entropy(text);

    return 1.0 - (actual_entropy / max_entropy);
}

int main() {
    string input;
    getline(cin, input);

    double entropy = calculate_entropy(input);
    double redundancy = calculate_redundancy(input);

    cout << fixed << setprecision(6);
    cout << entropy << endl;
    cout << redundancy << endl;

    return 0;
}