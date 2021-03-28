class Solution {
public:
    uint32_t reverse_bits(uint32_t n) {
        uint32_t rev = 0;
        for (int i = 0; i < 32 && n > 0; ++i) {
            rev |= (n & i) << (32 - i);
            n >>= 1;
        }
        return rev;
    }
};