#!/usr/bin/env python3
"""Test script for entropy and redundancy calculations."""
import math

def calculate_entropy(text):
    if not text:
        return 0.0
    freq = {}
    for c in text:
        freq[c] = freq.get(c, 0) + 1
    entropy = 0.0
    for count in freq.values():
        p = count / len(text)
        entropy -= p * math.log2(p)
    return entropy

def calculate_redundancy(text, alphabet_size=256):
    if not text:
        return 0.0
    max_entropy = math.log2(alphabet_size)
    actual_entropy = calculate_entropy(text)
    return max_entropy - actual_entropy

def mod_inverse(a, m):
    """Calculate modular inverse using extended Euclidean algorithm."""
    def extended_euclid(a, b):
        if b == 0:
            return a, 1, 0
        g, x1, y1 = extended_euclid(b, a % b)
        x = y1
        y = x1 - (a // b) * y1
        return g, x, y
    
    g, x, y = extended_euclid(a, m)
    if g != 1:
        return -1
    return (x % m + m) % m

if __name__ == "__main__":
    print("=== Testing Entropy and Redundancy ===")
    test_cases = ["aaaa", "abcd", "hello world"]
    for text in test_cases:
        entropy = calculate_entropy(text)
        redundancy = calculate_redundancy(text)
        print(f"Input: '{text}'")
        print(f"  Entropy: {entropy:.6f}")
        print(f"  Redundancy: {redundancy:.6f}")
        print()
    
    print("=== Testing Modular Inverse ===")
    test_cases_mod = [(3, 7), (10, 17), (6, 9)]
    for a, m in test_cases_mod:
        inv = mod_inverse(a, m)
        if inv == -1:
            print(f"a={a}, m={m} -> Không tồn tại nghịch đảo")
        else:
            check = (a * inv) % m
            print(f"a={a}, m={m} -> nghịch đảo = {inv}, kiểm tra: {a}*{inv} mod {m} = {check}")