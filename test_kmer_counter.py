import kmer_counter


class TestCount(object):
    def test_with_record_size_3_returns_kmer_size_3(self):
        # given
        record = 'AAA'

        # when
        count = kmer_counter.count(record)

        # then
        assert list(count.keys()) == [record]
        assert list(count.values()) == [1]
