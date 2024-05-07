import scripts.create_activity_table
import scripts.create_database
import scripts.create_view
import scripts.create_user
import scripts.grant_permissions
import scripts.ensure_ordering
import scripts.set_role
import scripts.set_timezone
import scripts.set_buffer_pool_size
import scripts.set_max_connections

# Spuštění všech úkolů
scripts.create_user()
scripts.grant_permissions()
scripts.set_role()
scripts.create_database()
"""scripts.create_activity_table.main()
scripts.create_view.main()
scripts.grant_permissions.main()
scripts.ensure_ordering.main()
scripts.set_timezone.main()
scripts.set_buffer_pool_size.main()
scripts.set_max_connections.main()
"""