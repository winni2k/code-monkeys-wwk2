import collections
import argparse


def count(record, kmer_size):
    counts = collections.defaultdict(lambda: 0)
    assert kmer_size > 0
    assert len(record) >= kmer_size
    for kmer_idx in range(len(record) - kmer_size + 1):
        counts[record[kmer_idx:(kmer_idx + kmer_size)]] += 1
    return counts


FastaRecord = collections.namedtuple('FastaRecord', ['desc', 'seq'])


def fasta_records(fasta_handle):
    for description in fasta_handle:
        record = next(fasta_handle)

        yield FastaRecord(desc=description[1:].rstrip(), seq=record.rstrip())


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Kmer counter')
    parser.add_argument('fasta')
    parser.add_argument('--kmer-size', default=3)

    args = parser.parse_args()

    with open(args.fasta) as file_handle:
        for record in fasta_records(file_handle):
            print(count(record, args.kmer_size))
