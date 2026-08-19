class Align:
    miss_score = -1
    match_score = +1
    gap_score = -2
    mode = "local"

    def __init__(self):
        pass

    def align(self, seq1, seq2):
        if self.mode == "local":
            #smith-Waterman-Algorithm
            rows = len(seq1) + 1
            cols = len(seq2) + 1

            score_matrix = [[0 for _ in range(cols)] for _ in range(rows)]
            traceback_matrix = [["0" for _ in range(cols)] for _ in range(rows)]

            max_score = 0
            max_position = (0, 0)

            for i in range(1, rows):
                for j in range(1, cols):

                    if seq1[i - 1] == seq2[j - 1]:
                        diagonal_score = score_matrix[i - 1][j - 1] + self.match_score
                    else:
                        diagonal_score = score_matrix[i - 1][j - 1] + self.miss_score

                    up_score = score_matrix[i - 1][j] + self.gap_score
                    left_score = score_matrix[i][j - 1] + self.gap_score

                    best_score = max(0, diagonal_score, up_score, left_score)

                    score_matrix[i][j] = best_score

                    if best_score == 0:
                        traceback_matrix[i][j] = "0"
                    elif best_score == diagonal_score:
                        traceback_matrix[i][j] = "D"
                    elif best_score == up_score:
                        traceback_matrix[i][j] = "U"
                    else:
                        traceback_matrix[i][j] = "L"

                    if best_score > max_score:
                        max_score = best_score
                        max_position = (i, j)

            aligned_seq1 = []
            aligned_seq2 = []

            i, j = max_position

            while traceback_matrix[i][j] != "0":
                direction = traceback_matrix[i][j]

                if direction == "D":
                    aligned_seq1.append(seq1[i - 1])
                    aligned_seq2.append(seq2[j - 1])
                    i -= 1
                    j -= 1

                elif direction == "U":
                    aligned_seq1.append(seq1[i - 1])
                    aligned_seq2.append("-")
                    i -= 1

                elif direction == "L":
                    aligned_seq1.append("-")
                    aligned_seq2.append(seq2[j - 1])
                    j -= 1

            aligned_seq1 = "".join(reversed(aligned_seq1))
            aligned_seq2 = "".join(reversed(aligned_seq2))

            return aligned_seq1, aligned_seq2, max_score, score_matrix

        else:
            #Nedleman-Wunsch-Algorithm
            m = len(seq1)
            n = len(seq2)

            score_matrix = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

            for i in range(1, m + 1):
                score_matrix[i][0] = score_matrix[i - 1][0] + self.gap_score

            for j in range(1, n + 1):
                score_matrix[0][j] = score_matrix[0][j - 1] + self.gap_score

            for i in range(1, m + 1):
                for j in range(1, n + 1):
                    if seq1[i - 1] == seq2[j - 1]:
                        diagonal_score = score_matrix[i - 1][j - 1] + self.match_score
                    else:
                        diagonal_score = score_matrix[i - 1][j - 1] + self.miss_score

                    up_score = score_matrix[i - 1][j] + self.gap_score
                    left_score = score_matrix[i][j - 1] + self.gap_score

                    score_matrix[i][j] = max(diagonal_score, up_score, left_score)

            aligned_seq1 = ""
            aligned_seq2 = ""

            i = m
            j = n

            while i > 0 and j > 0:
                current_score = score_matrix[i][j]

                if seq1[i - 1] == seq2[j - 1]:
                    score = self.match_score
                else:
                    score = self.miss_score

                if current_score == score_matrix[i - 1][j - 1] + score:
                    aligned_seq1 = seq1[i - 1] + aligned_seq1
                    aligned_seq2 = seq2[j - 1] + aligned_seq2
                    i -= 1
                    j -= 1

                elif current_score == score_matrix[i - 1][j] + self.gap_score:
                    aligned_seq1 = seq1[i - 1] + aligned_seq1
                    aligned_seq2 = "-" + aligned_seq2
                    i -= 1

                else:
                    aligned_seq1 = "-" + aligned_seq1
                    aligned_seq2 = seq2[j - 1] + aligned_seq2
                    j -= 1

            while i > 0:
                aligned_seq1 = seq1[i - 1] + aligned_seq1
                aligned_seq2 = "-" + aligned_seq2
                i -= 1

            while j > 0:
                aligned_seq1 = "-" + aligned_seq1
                aligned_seq2 = seq2[j - 1] + aligned_seq2
                j -= 1

            return aligned_seq1, aligned_seq2, score_matrix[m][n], score_matrix


if __name__ == "__main__":
    a = Align()
    # a.mode = "local"
    # print(a.align("GGATCAGTACGTTACCGGAT", "TTACGATACCGTTAAGG"))

    a.mode = "global"
    print(a.align("GATTACA", "GCATGCU"))