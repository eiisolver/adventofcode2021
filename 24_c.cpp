#include <cstdint>
#include <vector>
#include <cstdio>
#include <unordered_set>

using namespace std;

long long w, x, y, z;

using Func = long long (*)(long long, int);

long long f0(long long z0, int input) {
    z = z0;
    w = input;
    x *= 0;
    x += z;
    x = x % 26;
    z /= 1;
    x += 14;
    x = x == w ? 1 : 0;
    x = x == 0 ? 1 : 0;
    y *= 0;
    y += 25;
    y *= x;
    y += 1;
    z *= y;
    y *= 0;
    y += w;
    y += 12;
    y *= x;
    z += y;
    return z;
}

long long f1(long long z0, int input) {
    z = z0;
    w = input;
    x *= 0;
    x += z;
    x = x % 26;
    z /= 1;
    x += 15;
    x = x == w ? 1 : 0;
    x = x == 0 ? 1 : 0;
    y *= 0;
    y += 25;
    y *= x;
    y += 1;
    z *= y;
    y *= 0;
    y += w;
    y += 7;
    y *= x;
    z += y;
    return z;
}

long long f2(long long z0, int input) {
    z = z0;
    w = input;
    x *= 0;
    x += z;
    x = x % 26;
    z /= 1;
    x += 12;
    x = x == w ? 1 : 0;
    x = x == 0 ? 1 : 0;
    y *= 0;
    y += 25;
    y *= x;
    y += 1;
    z *= y;
    y *= 0;
    y += w;
    y += 1;
    y *= x;
    z += y;
    return z;
}

long long f3(long long z0, int input) {
    z = z0;
    w = input;
    x *= 0;
    x += z;
    x = x % 26;
    z /= 1;
    x += 11;
    x = x == w ? 1 : 0;
    x = x == 0 ? 1 : 0;
    y *= 0;
    y += 25;
    y *= x;
    y += 1;
    z *= y;
    y *= 0;
    y += w;
    y += 2;
    y *= x;
    z += y;
    return z;
}

long long f4(long long z0, int input) {
    z = z0;
    w = input;
    x *= 0;
    x += z;
    x = x % 26;
    z /= 26;
    x += -5;
    x = x == w ? 1 : 0;
    x = x == 0 ? 1 : 0;
    y *= 0;
    y += 25;
    y *= x;
    y += 1;
    z *= y;
    y *= 0;
    y += w;
    y += 4;
    y *= x;
    z += y;
    return z;
}

long long f5(long long z0, int input) {
    z = z0;
    w = input;
    x *= 0;
    x += z;
    x = x % 26;
    z /= 1;
    x += 14;
    x = x == w ? 1 : 0;
    x = x == 0 ? 1 : 0;
    y *= 0;
    y += 25;
    y *= x;
    y += 1;
    z *= y;
    y *= 0;
    y += w;
    y += 15;
    y *= x;
    z += y;
    return z;
}

long long f6(long long z0, int input) {
    z = z0;
    w = input;
    x *= 0;
    x += z;
    x = x % 26;
    z /= 1;
    x += 15;
    x = x == w ? 1 : 0;
    x = x == 0 ? 1 : 0;
    y *= 0;
    y += 25;
    y *= x;
    y += 1;
    z *= y;
    y *= 0;
    y += w;
    y += 11;
    y *= x;
    z += y;
    return z;
}

long long f7(long long z0, int input) {
    z = z0;
    w = input;
    x *= 0;
    x += z;
    x = x % 26;
    z /= 26;
    x += -13;
    x = x == w ? 1 : 0;
    x = x == 0 ? 1 : 0;
    y *= 0;
    y += 25;
    y *= x;
    y += 1;
    z *= y;
    y *= 0;
    y += w;
    y += 5;
    y *= x;
    z += y;
    return z;
}

long long f8(long long z0, int input) {
    z = z0;
    w = input;
    x *= 0;
    x += z;
    x = x % 26;
    z /= 26;
    x += -16;
    x = x == w ? 1 : 0;
    x = x == 0 ? 1 : 0;
    y *= 0;
    y += 25;
    y *= x;
    y += 1;
    z *= y;
    y *= 0;
    y += w;
    y += 3;
    y *= x;
    z += y;
    return z;
}

long long f9(long long z0, int input) {
    z = z0;
    w = input;
    x *= 0;
    x += z;
    x = x % 26;
    z /= 26;
    x += -8;
    x = x == w ? 1 : 0;
    x = x == 0 ? 1 : 0;
    y *= 0;
    y += 25;
    y *= x;
    y += 1;
    z *= y;
    y *= 0;
    y += w;
    y += 9;
    y *= x;
    z += y;
    return z;
}

long long f10(long long z0, int input) {
    z = z0;
    w = input;
    x *= 0;
    x += z;
    x = x % 26;
    z /= 1;
    x += 15;
    x = x == w ? 1 : 0;
    x = x == 0 ? 1 : 0;
    y *= 0;
    y += 25;
    y *= x;
    y += 1;
    z *= y;
    y *= 0;
    y += w;
    y += 2;
    y *= x;
    z += y;
    return z;
}

long long f11(long long z0, int input) {
    z = z0;
    w = input;
    x *= 0;
    x += z;
    x = x % 26;
    z /= 26;
    x += -8;
    x = x == w ? 1 : 0;
    x = x == 0 ? 1 : 0;
    y *= 0;
    y += 25;
    y *= x;
    y += 1;
    z *= y;
    y *= 0;
    y += w;
    y += 3;
    y *= x;
    z += y;
    return z;
}

long long f12(long long z0, int input) {
    z = z0;
    w = input;
    x *= 0;
    x += z;
    x = x % 26;
    z /= 26;
    x += 0;
    x = x == w ? 1 : 0;
    x = x == 0 ? 1 : 0;
    y *= 0;
    y += 25;
    y *= x;
    y += 1;
    z *= y;
    y *= 0;
    y += w;
    y += 3;
    y *= x;
    z += y;
    return z;
}

long long f13(long long z0, int input) {
    z = z0;
    w = input;
    x *= 0;
    x += z;
    x = x % 26;
    z /= 26;
    x += -4;
    x = x == w ? 1 : 0;
    x = x == 0 ? 1 : 0;
    y *= 0;
    y += 25;
    y *= x;
    y += 1;
    z *= y;
    y *= 0;
    y += w;
    y += 11;
    y *= x;
    z += y;
    return z;
}

vector<Func> funcs {f0, f1, f2, f3, f4, f5, f6, f7, f8, f9, f10, f11, f12, f13};

void clear() {
    w = 0;
    x = 0;
    y = 0;
    z = 0;
}

void print_vars() {
    printf("w=%lld,x=%lld,y=%lld,z=%lld\n", w, x, y, z);
}

long long f(int ix, long long z0, int input) {
    clear();
    return funcs[ix](z0, input);
}

int main() {
    vector<unordered_set<long long>> solutions(14);
    solutions[13].insert(0);
    long long upper = 1;
    // Start backward to find inputs that yield z = 0
    for (int ix = 13; ix >= 4; --ix) {
        printf("Backward: input %d\n", ix);
        constexpr long long MAX = 30000000;
        if (upper < MAX) {
            upper *= 26;
        }
        unordered_set<long long> &new_solutions = solutions[ix-1];
        for (long long z0 = 0; z0 < std::min(upper, MAX); ++z0) {
            for (int i = 1; i <= 9; ++i) {
                clear();
                int z2 = f(ix, z0, i);
                if (solutions[ix].count(z2)) {
                    new_solutions.insert(z0);
                }
            }
        }
    }
    vector<int> highest;
    vector<int> smallest;
    for (int a = 1; a <= 9; ++a) {
        for (int b = 1; b <= 9; ++b) {
            for (int c = 1; c <= 9; ++c) {
                for (int d = 1; d <= 9; ++d) {
                    int z = f(0, 0, a);
                    z = f(1, z, b);
                    z = f(2, z, c);
                    z = f(3, z, d);
                    if (solutions[3].count(z)) {
                        printf("Possible first 4 digits: %d, %d, %d, %d\n", a, b, c, d);
                        highest.clear();
                        highest.push_back(a);
                        highest.push_back(b);
                        highest.push_back(c);
                        highest.push_back(d);
                        if (smallest.empty()) {
                            smallest = highest;
                        }
                    }
                }
            }
        }
    }
    long long z = 0;
    for (int i = 0; i < 4; ++i) {
        z = f(i, z, highest[i]);
    }
    for (int i = 4; i < 14; ++i) {
        for (int j = 9; j >= 1; --j) {
            long long z2 = f(i, z, j);
            if (solutions[i].count(z2)) {
                z = z2;
                highest.push_back(j);
                break;
            }
        }
    }
    //highest = { 1, 2, 9, 9, 6, 9, 9, 7, 8, 2, 9, 3, 9, 9  };
    printf("Largest: ");
    for (auto n : highest) {
        printf("%d, ", n);
    }
    printf("\n");
    z = 0;
    for (int i = 0; i < 4; ++i) {
        z = f(i, z, smallest[i]);
    }
    for (int i = 4; i < 14; ++i) {
        for (int j = 1; j <= 9; ++j) {
            long long z2 = f(i, z, j);
            if (solutions[i].count(z2)) {
                z = z2;
                smallest.push_back(j);
                break;
            }
        }
    }
    printf("Smallest: ");
    for (auto n : smallest) {
        printf("%d, ", n);
    }
    printf("\n");
    //smallest = {1, 1, 8, 4, 6, 2, 3, 1, 1, 2, 7, 1, 9, 9};

    return 0;
}
