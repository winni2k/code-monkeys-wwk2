import collections


def count(record, kmer_size):
    counts = collections.defaultdict(lambda: 0)
    assert kmer_size > 0
    assert len(record) >= kmer_size
    for kmer_idx in range(len(record) - kmer_size + 1):
        counts[record[kmer_idx:(kmer_idx + kmer_size)]] += 1
    return counts
