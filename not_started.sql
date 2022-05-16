-- find number of learners who have enrolled into HPTO but have not started the real HPTO test at least once
select
    user_id,
    min(created_at) as enrolled
from
    progress.events
where
    module_id = 'some_id'
    -- and course_id is not null
    and user_id not in (
        select
            user_id
        from
            progress.events
        where
            module_id = 'some_id'
            and (
                status = 'FAILED'
                or status = 'PASSED'
                or status = 'IN_PROGRESS'
            )
        group by
            user_id
    )
group by
    user_id
order by
    enrolled