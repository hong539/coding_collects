--src: https://hackmd.io/@pgsql-tw/rJSOHh8zT
with t1 as MATERIALIZED (
select array_agg(tag_id) as tag_ids
  from tags
 where tag_name in ('熟女', '巨乳', '泳裝')
)
select va.vid_number
  from videos_array va
  join t1
    on va.vid_tags @> t1.tag_ids;