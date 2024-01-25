def study_schedule(permanence_period, target_time):
    if target_time is None:
        return None

    students_online = 0

    for temp_in, temp_out in permanence_period:
        if (
            temp_in is None
            or temp_out is None
            or not isinstance(temp_in, int)
            or not isinstance(temp_out, int)
        ):
            return None

        if isinstance(target_time, int) and temp_in <= target_time <= temp_out:
            students_online += 1

    return students_online
