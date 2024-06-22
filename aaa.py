def main():
    test_scores = []

    for i in range(10):
        while True:
            try:
                score = float(input(f"input score {i + 1}: "))
                if score > 100:
                    print("error. input again")
                    continue
                test_scores.append(score)
                break
            except ValueError:
                print("input score")
    sorted_scores = sorted(test_scores)

    new_array = sorted_scores[2:]

    average_score = sum(test_scores) / len(test_scores)
    average_score_after_removal = sum(new_array) / len(new_array)

    # In kết quả
    print(f"Điểm thấp nhất: {sorted_scores[0]}")
    print(f"Điểm cao nhất : {sorted_scores[-1]}")
    print(f"Điểm lớn thứ 2 : {sorted_scores[-2]}")
    print(f"Trung bình : {average_score:.2f}")
    print(f"Trung bình sau khi loại bỏ hai số nhỏ nhất : {average_score_after_removal:.2f}")

if __name__ == "__main__":
    main()
