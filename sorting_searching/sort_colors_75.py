def sort_colors(nums):
    n = len(nums)
    if n == 0:
        return
    last_0_idx = -1  # this is NOT the pythonic index, this is "before 0 index".
    last_1_idx = None
    for idx in range(n):
        if nums[idx] == 0:
            # place this zero after the last zero
            if nums[last_0_idx + 1] == 1:
                if last_1_idx is None:
                    last_1_idx = last_0_idx
                # TODO: what if there is no last_1_idx
                nums[idx], nums[last_0_idx + 1], nums[last_1_idx + 1] = (
                    nums[last_1_idx + 1],
                    nums[idx],
                    nums[last_0_idx + 1],
                )
                last_1_idx += 1
            if nums[last_0_idx + 1] == 2:
                nums[idx], nums[last_0_idx + 1] = nums[last_0_idx + 1], nums[idx]
            last_0_idx += 1
        elif nums[idx] == 1:
            if last_1_idx is None:
                last_1_idx = last_0_idx
            nums[idx], nums[last_1_idx + 1] = nums[last_1_idx + 1], nums[idx]
            last_1_idx += 1
