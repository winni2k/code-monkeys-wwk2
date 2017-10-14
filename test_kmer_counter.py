import pytest

import kmer_counter


class TestCount(object):
    def test_with_empty_record_raises(self):
        with pytest.raises(AssertionError):
            kmer_counter.count('', 3)

    def test_with_kmer_size_0_raises(self):
        with pytest.raises(AssertionError):
            kmer_counter.count('A', 0)

    def test_with_record_length_2_and_kmer_length_3_raises(self):
        with pytest.raises(AssertionError):
            kmer_counter.count('AA', 3)

    def test_with_record_size_3_returns_kmer_size_3(self):
        # given
        record = 'AAA'

        # when
        count = kmer_counter.count(record, 3)

        # then
        assert list(count.keys()) == [record]
        assert list(count.values()) == [1]

    def test_with_record_size_4_returns_one_kmer_count_2(self):
        # given
        record = 'AAAA'
        kmer_size = 3
        # when
        count = kmer_counter.count(record, kmer_size)

        # then
        assert list(count.keys()) == [record[:kmer_size]]
        assert list(count.values()) == [2]

    def test_with_two_kmers_returns_two_kmers_size_3(self):
        # given
        record = 'AAAT'
        kmer_size = 3
        # when
        count = kmer_counter.count(record, kmer_size)

        # then
        assert count['AAA'] == 1
        assert count['AAT'] == 1

    def test_with_two_kmers_returns_two_kmers_size_1(self):
        # given
        record = 'AT'
        kmer_size = 1
        # when
        count = kmer_counter.count(record, kmer_size)

        # then
        assert count['A'] == 1
        assert count['T'] == 1



