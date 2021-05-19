## Open Redirection Related dork

site:*.example.com inurl:redirect | inurl:redirect_to | inurl:redirect_uri

- inurl:request= | inurl:src= | inurl:jump= | inurl:forward= | inurl:goto=

- inurl:url=https | inurl:url=http | inurl:redirect?https | inurl:redirect?http | inurl:redirect=https | inurl:redirect=http | inurl:link=http | inurl:link=https

- inurl:u= | inurl:r= | inurl:=http | inurl:next= | inurl:=?imageurl= | inurl:continue= | inurl:target= ------>>> Dork related with redirection (related report https://medium.com/@nandwanajatin25/story-of-a-uri-based-xss-with-some-simple-google-dorking-e1999254aa55)

### Note:
Don't underestimate open redirection vulnerability you may chain this with xss,ssrf,Oauth flow,csrf,Referrer check bypass ect}

## Email Related Dorks

- site:target.com inurl:email                                                                                                                                                                                                        
- filetype:xls inurl:"email.xls" site:.bd  

- site:.edu filetype:xls inurl:"email.xls"
                                               
- site:target.com inurl:'@yahoo.com'
                                            
- site:target.com inurl:'@live.com'            

- site:target.com inurl:'@gmail.com'          

### Note: 
To specific country you can also use .uk or .pk or .bd ect

### Author:

Linkdin: [@tamimhasan404](https://www.linkedin.com/in/tamimhasan404/)
Github: [@tamimhasan404](https://github.com/tamimhasan404)
Medium: [@tamimhasan404](https://tamimhasan404.medium.com/)
Twitter: [@tamimhasan404](https://twitter.com/tamimhasan404)
