--src: https://hackmd.io/@pgsql-tw/rJSOHh8zT
select v.vid_number
  from videos v
  join video_tags vt1
    on (v.vid_id = vt1.vid_id)
  join video_tags vt2
    on (vt1.vid_id = vt2.vid_id)
  join tags t1
    on (vt1.tag_id = t1.tag_id)
  join tags t2
    on (vt2.tag_id = t2.tag_id)
 where t1.tag_name = '熟女'
   and t2.tag_name = '巨乳';