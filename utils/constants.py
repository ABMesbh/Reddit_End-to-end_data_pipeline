import configparser
import os 

parser = configparser.ConfigParser()
parser.read(os.path.join(os.path.dirname(__file__), '../config/config.conf'))

Secret = parser.get('api_keys', 'reddit_secret_key')
Client_id = parser.get('api_keys', 'reddit_client_id')


Database_host = parser.get('database', 'database_host')
Database_name = parser.get('database', 'database_name')
Database_port = parser.get('database', 'database_port')
Database_user = parser.get('database', 'database_username')
Database_password = parser.get('database', 'database_password')

Input_path = parser.get('file_paths', 'input_path')
Output_path = parser.get('file_paths', 'output_path')

# AWS 
Aws_access_key_id = parser.get('aws', 'aws_access_key_id')
Aws_secret_key = parser.get('aws', 'aws_secret_access_key')
Aws_region = parser.get('aws', 'aws_region')
Aws_bucket_name = parser.get('aws', 'aws_bucket_name')

# {'comment_limit': 2048, 'comment_sort': 'confidence', '_reddit': <praw.reddit.Reddit object at 0x7f577f036bb0>, 'approved_at_utc': None, 'subreddit': Subreddit(display_name='dataengineering'), 'selftext': 'I have an interview tomorrow. \n\n1 hour management interview (in which I believe I’ll be very comfortable)\nFollowed by \n1 hour tech interview (not so confident)\n\nA little about me: I have consulting experience, know SQL, R & have worked on Tableau. \n\nThe role: Data Quality Lead\n\nCan send the JD in chat.', 'author_fullname': 't2_bo6y7ima3', 'saved': False, 'mod_reason_title': None, 'gilded': 0, 'clicked': False, 'title': 'Interview Tomorrow. Need Collibra Crash Course!', 'link_flair_richtext': [], 'subreddit_name_prefixed': 'r/dataengineering', 'hidden': False, 'pwls': 6, 'link_flair_css_class': '', 'downs': 0, 'thumbnail_height': None, 'top_awarded_type': None, 'hide_score': False, 'name': 't3_17ixs5d', 'quarantine': False, 'link_flair_text_color': 'light', 'upvote_ratio': 0.4, 'author_flair_background_color': None, 'subreddit_type': 'public', 'ups': 0, 'total_awards_received': 0, 'media_embed': {}, 'thumbnail_width': None, 'author_flair_template_id': None, 'is_original_content': False, 'user_reports': [], 'secure_media': None, 'is_reddit_media_domain': False, 'is_meta': False, 'category': None, 'secure_media_embed': {}, 'link_flair_text': 'Help', 'can_mod_post': False, 'score': 0, 'approved_by': None, 'is_created_from_ads_ui': False, 'author_premium': False, 'thumbnail': 'self', 'edited': False, 'author_flair_css_class': None, 'author_flair_richtext': [], 'gildings': {}, 'content_categories': None, 'is_self': True, 'mod_note': None, 'created': 1698564853.0, 'link_flair_type': 'text', 'wls': 6, 'removed_by_category': None, 'banned_by': None, 'author_flair_type': 'text', 'domain': 'self.dataengineering', 'allow_live_comments': False, 'selftext_html': '<!-- SC_OFF --><div class="md"><p>I have an interview tomorrow. </p>\n\n<p>1 hour management interview (in which I believe I’ll be very comfortable)\nFollowed by \n1 hour tech interview (not so confident)</p>\n\n<p>A little about me: I have consulting experience, know SQL, R &amp; have worked on Tableau. </p>\n\n<p>The role: Data Quality Lead</p>\n\n<p>Can send the JD in chat.</p>\n</div><!-- SC_ON -->', 'likes': None, 'suggested_sort': None, 'banned_at_utc': None, 'view_count': None, 'archived': False, 'no_follow': True, 'is_crosspostable': False, 'pinned': False, 'over_18': False, 'all_awardings': [], 'awarders': [], 'media_only': False, 'link_flair_template_id': '2ca94cd6-ac27-11eb-a8eb-0e7f457f5bd3', 'can_gild': False, 'spoiler': False, 'locked': False, 'author_flair_text': None, 'treatment_tags': [], 'visited': False, 'removed_by': None, 'num_reports': None, 'distinguished': None, 'subreddit_id': 't5_36en4', 'author_is_blocked': False, 'mod_reason_by': None, 'removal_reason': None, 'link_flair_background_color': '#ea0027', 'id': '17ixs5d', 'is_robot_indexable': True, 'report_reasons': None, 'author': Redditor(name='zamonk8'), 'discussion_type': None, 'num_comments': 1, 'send_replies': True, 'whitelist_status': 'all_ads', 'contest_mode': False, 'mod_reports': [], 'author_patreon_flair': False, 'author_flair_text_color': None, 'permalink': '/r/dataengineering/comments/17ixs5d/interview_tomorrow_need_collibra_crash_course/', 'parent_whitelist_status': 'all_ads', 'stickied': False, 'url': 'https://www.reddit.com/r/dataengineering/comments/17ixs5d/interview_tomorrow_need_collibra_crash_course/', 'subreddit_subscribers': 136697, 'created_utc': 1698564853.0, 'num_crossposts': 0, 'media': None, 'is_video': False, '_fetched': False, '_additional_fetch_params': {}, '_comments_by_id': {}}

Post_fields = (
    'id', 
    'title',
    'score',
    'author',
    'created_utc',
    'url',
    'upvote_ratio',
    'over_18',
    'edited',
    'spoiler',
    'stickied','num_comments'

)