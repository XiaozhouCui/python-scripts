-- list the clientUserId of learners who have either 'Failed' or 'Incomplete' HPTO but have NOT yet 'Passed'
select
    user_id,
    min(created_at) as enrolled
from
    progress.events
where
    module_id = 'some_id'
    and course_id is not null
    and user_id not in (
        select
            user_id
        from
            progress.events
        where
            module_id = 'some_id'
            and status = 'PASSED'
        group by
            user_id
    )
group by
    user_id
order by
    enrolled