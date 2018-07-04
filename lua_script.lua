function main(splash, args)
  assert(splash:go(args.url))
  assert(splash:wait(3.0))
  submit = splash:select('a.more')
  count = 1
  while (submit and count < 10000) do
    if count%10 == 0 then
      splash:wait(10)
      print(count)
    end
    submit:mouse_click()
    splash:wait(2.0)
    submit = splash:select('a.more')
    count = count + 1
  end
  return {
    html = splash:html(),
    png = splash:png(),
    har = splash:har()
  }
end
