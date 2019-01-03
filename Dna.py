import warnings

class Dna:
    """
    A class used to represent an immutable DNA strand

    ...

    Attributes
    ----------
    sequence : str
        a sequence, made of characters A, G, C, T
    rc : str
        the reverse of sequence with its characters switched
        with their complementary character which are
        A = T, G = C, C = G, T = A

    Methods
    -------
    __init__(seq = None)
        Initializes Dna with a string sequence defined by
        parameter seq or, if no parameters are passed,
        the string None
    get_skew()
        Returns the skew of C:G at each position in sequence
    get_length()
        Returns the lenght of sequence
    """

    BASES = ("A","G","C","T")
    MATCHES = {'A':'T', 'C':'G', 'G':'C', 'T':'A'}


    def __init__(self, seq = None):
        """Initializes Dna from a sequence of BASES.

        Parameters
        ----------
        seq : str, optional
            The Dna sequence, made of characters in BASES.
            If a sequence is not passed, the default string
            None is used.

        Raises
        ------
        ValueError
            Occurs if the sequence is not made of the
            characters in BASES, "A"(or "a"), "G"(or "g"),
            "C"(or "c"), "T"(or "t").

            Occurs if seq = None. A Dna strand must contain
            at least 1 base.
        """

        if seq == None:
            raise ValueError("Invalid Dna strand. Contains no sequence.")

        for i in seq.upper(): #dna must be made of BASES
            if i in self.BASES:
                pass
            else:
                raise ValueError("Invalid DNA sequence. Must consist of" \
                + " bases %s" % (" ".join(self.BASES)))

        self.sequence = seq.upper()
        self.rc = ''.join(self.MATCHES[x] for x in self.sequence[::-1])
        self.skew = self.get_skew()
        self.lenght = self.get_length()

    # def get_rc(self):
    #     """Returns reverse complement of sequence
    #
    #     Returns
    #     ------
    #     The reverse complement of sequence, which is derived
    #     by first reversing sequence and then replacing each
    #     character with its key in MATCHES.
    #     """
    #
    #     return ''.join(self.MATCHES[x] for x in self.sequence[::-1])

    def get_skew(self):
        """Returns the skew

        Returns
        ------
        skew : The list representing the skew of C : G
        at each base along sequence.
        """

        MAP = {'A':0, 'T':0, 'C':-1, 'G':1}
        skew = []
        for if, value in enumerate(self):
            skew.append(skew[i] + MAP[value])
        return skew

    def get_length(self):
        """Returns the length

        Returns
        ------
        length : the length of sequence
        """

        return sequence.length()
