import matplotlib.pyplot as plt


class Sequence:
    def __init__(self, name, sequence):
        self.name = name
        self.sequence = sequence.upper()   # vždy uložíme velkými písmeny

    def length(self):
        return len(self.sequence)

    def __str__(self):
        return f"[{self.name}] délka={self.length()} nt, začátek: {self.sequence[:8]}..."

class DNASequence(Sequence):
    def gc_content(self):
        gc = self.sequence.count("G") + self.sequence.count("C")
        return gc / len(self.sequence)

    def base_counts(self):
        return {
            "A": self.sequence.count("A"),
            "C": self.sequence.count("C"),
            "G": self.sequence.count("G"),
            "T": self.sequence.count("T"),
        }

    def plot_composition(self):
        counts = self.base_counts()
        bases = ["A", "C", "G", "T"]
        values = [counts[b] for b in bases]
        colors = ["tab:green", "tab:blue", "tab:orange", "tab:red"]

        plt.figure(figsize=(5, 3))
        plt.bar(bases, values, color=colors, edgecolor="black")
        plt.title(f"Složení bází: {self.name}")
        plt.ylabel("Počet")
        plt.tight_layout()
        plt.show()

    def is_valid(self):
        return set(self.sequence) <= {"A", "C", "G", "T"}

    # Transkripce DNA → RNA
    def to_rna(self):
        return RNASequence(self.name, self.sequence.replace("T", "U"))

class RNASequence(Sequence):

    # Validace RNA
    def is_valid(self):
        return set(self.sequence) <= {"A", "C", "G", "U"}


# Rozdělení na kodony
    def codons(self):
        return [self.sequence[i:i+3] for i in range(0, len(self.sequence) - 2, 3)]


    # Hledání start kodonu AUG
    def find_start_codon(self):
        return self.sequence.find("AUG")

dna = DNASequence("gen_01", "CCATGGCTTAA")

rna = dna.to_rna()
print(rna)
print(rna.is_valid())
print(rna.find_start_codon())
print(rna.codons())
