--src: https://hackmd.io/@pgsql-tw/rJSOHh8zT
select v.vid_number
  from videos v
  join video_tags vt
    on (v.vid_id = vt.vid_id)
  join tags t
    on (vt.tag_id = t.tag_id)
 where t.tag_name = '女教師';