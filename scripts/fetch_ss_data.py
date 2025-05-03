<!-- _includes/fetch_citations.html -->
<script>
  document.addEventListener('DOMContentLoaded', () => {
    // Jekyll 会把 _data/ss_data.json 输出到 /ss_data.json
    const ssUrl = '{{ site.baseurl }}/ss_data.json';

    fetch(ssUrl)
      .then(r => {
        if (!r.ok) throw new Error('SS JSON 读取失败：' + r.status);
        return r.json();
      })
      .then(ssData => {
        document.querySelectorAll('.show_paper_citations[data-doi]').forEach(el => {
          const doi = el.getAttribute('data-doi');
          const ssCount = ssData[doi];
          if (ssCount != null) {
            // 插入 "| Citations: 15"
            el.insertAdjacentHTML('beforeend', ` | Citations: ${ssCount}`);
          }
        });
      })
      .catch(err => console.error('Semantic Scholar 数据拉取出错：', err));
  });
</script>