
# Candy.
# https://leetcode.com/problems/candy/


def candy(ratings: list[int]) -> int:
    
    def is_satisfy(r: list[int], c: list[int]) -> bool: 
        pass

    candy = [1] * len(ratings)
    while True:
        is_satisfy = True
        for i in range(len(ratings)):
            current_candy = candy[i]
            current_rating = ratings[i]

            if i > 0 and current_rating > ratings[i-1] and current_candy <= candy[i-1]:
                candy[i] += 1
                is_satisfy = False
            if i < len(ratings)-1 and current_rating > ratings[i+1] and current_candy <= candy[i+1]:
                candy[i] += 1
                is_satisfy = False

        if is_satisfy:
            break
    
    # debug.
    #print(candy)

    return sum(candy)


print(candy([1,0,2]))  # 5.
print(candy([1,2,2]))  # 4.
